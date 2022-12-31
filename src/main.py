"""
pyqt5 App for pm4py

author: boer
last edited: 2022-12-29
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction, qApp, QMenu, QFileDialog, QMessageBox, QGraphicsView, QGraphicsScene, QGraphicsPixmapItem
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtCore import Qt
# QPattern
from shutil import copy
import pm4py
import os
import pandas
from ui.ui_mainwindow import Ui_MainWindow

# 工具类


class Utils:
    @staticmethod
    def get_all_files_in_dir(dir_path):
        return [os.path.join(dir_path, i) for i in os.listdir(dir_path)]

    @staticmethod
    def get_all_files_in_dir_by_type(dir_path, file_type):
        return [os.path.join(dir_path, i) for i in os.listdir(dir_path) if i.endswith(file_type)]

    @staticmethod
    def get_all_filenames_in_dir(dir_path):
        return [i for i in os.listdir(dir_path)]


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # 添加过程挖掘算法
        self.comboBox.addItems(
            ["alpha_miner", "heuristics_miner", "alpha_miner_plus", "inductive_miner"])
        self.comboBox_2.addItems(Utils.get_all_filenames_in_dir("./data"))
        self.actionimport_xes.triggered.connect(self.pop_up_open_files_window)
        self.actionimport_csv.triggered.connect(self.pop_up_open_files_window)
        self.actionopen_data_dir.triggered.connect(self.open_dir)

        self.pushButton.clicked.connect(self.pm4py_process_mining)

    def pop_up_open_files_window(self):
        fileNames, fileType = QFileDialog.getOpenFileNames(
            self, "选取文件", "./", "All Files (*);;CSV Files (*.csv);;XES Fioles(*.xes)")

        for i in fileNames:
            copy(i, "./data")
        # 刷新下拉框
        self.comboBox_2.clear()
        self.comboBox_2.addItems(Utils.get_all_filenames_in_dir("./data"))

    def open_dir(self):
        os.popen("explorer.exe .\\data")

    def pm4py_process_mining(self):
        log_path = "./data/" + self.comboBox_2.currentText()
        log = None
        # 读取日志
        if (log_path.endswith(".csv")):
            # # log = pm4py.read.read_ocel_csv(log_path)
            # # log = pandas.read_csv(log_path, sep=";")
            # log = pandas.read_csv(log_path)
            # log = pm4py.format_dataframe(log, case_id='case', activity_key='event', timestamp_key='timestamp')
            # start_activities = pm4py.get_start_activities(log)
            # end_activities = pm4py.get_end_activities(log)
            log = pandas.read_csv(log_path, sep=";")
            print(log)
            print(log.columns)
            print(log["case_id"])
            print(type(log["case_id"][0]))
            log["case_id"] = log["case_id"].astype(str)
            print(type(log["case_id"][0]))
            log = pm4py.format_dataframe(
                log, case_id='case_id', activity_key='activity', timestamp_key='timestamp')
            start_activities = pm4py.get_start_activities(log)
            end_activities = pm4py.get_end_activities(log)
            print("Start activities: {}\nEnd activities: {}".format(
                start_activities, end_activities))

        elif log_path.endswith(".xes"):
            log = pm4py.read_xes(log_path)
            start_activities = pm4py.get_start_activities(log)
            end_activities = pm4py.get_end_activities(log)
            print("Start activities: {}\nEnd activities: {}".format(
                start_activities, end_activities))

        # 选择算法
        algorithm = self.comboBox.currentText()
        print(algorithm)
        process_model = None
        net = None
        initial_marking = None
        final_marking = None
        if algorithm == "alpha_miner":
            net, initial_marking, final_marking = pm4py.discover_petri_net_alpha(
                log, activity_key="activity", timestamp_key="timestamp", case_id_key="case_id")
            print(process_model)
        elif algorithm == "heuristics_miner":
            process_model = pm4py.discover_heuristics_net(log)
        elif algorithm == "alpha_miner_plus":
            process_model = pm4py.discover_petri_net_alpha_plus(log)
        elif algorithm == "inductive_miner":
            process_model = pm4py.discover_petri_net_inductive(log)
        else:
            return
        # 将模型导出为图片
        gviz = pm4py.visualization.petri_net.visualizer.apply(
            net, initial_marking, final_marking)
        # gviz = pm4py.visualization.petri_net.visualizer.apply(process_model, "res/" + algorithm + ".png")
        # gviz = pm4py.visualization.petri_net.visualizer.apply(process_model, process_model["initial_marking"], process_model["final_marking"])
        # print(gviz)
        # 保存图片
        gviz.save("./res/" + algorithm)
        # 显示图片
        # pm4py.visualization.petri_net.visualizer.view(gviz)
        # 显示在GraphicsView中
        pixmap = QPixmap("./res/" + algorithm + ".png")
        scene = QGraphicsScene()
        scene.addPixmap(pixmap)
        self.graphicsView.setScene(scene)
        # # 设置允许使用鼠标滚轮缩放
        # self.graphicsView.setDragMode(QGraphicsView.ScrollHandDrag)
        # self.graphicsView.setInteractive(True)
        # self.graphicsView.setMouseTracking(True)
        # self.graphicsView.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        # self.graphicsView.setResizeAnchor(QGraphicsView.AnchorUnderMouse)
        # self.graphicsView.setRenderHint(QPainter.Antialiasing)
        # self.graphicsView.setRenderHint(QPainter.SmoothPixmapTransform)
        # self.graphicsView.setRenderHint(QPainter.HighQualityAntialiasing)
        # self.graphicsView.setRenderHint(QPainter.TextAntialiasing)
        # self.graphicsView.setRenderHint(QPainter.LosslessImageRendering)
        # self.graphicsView.setRenderHint(QPainter.NonCosmeticDefaultPen)

        # # 启用缩放功能
        # self.graphicsView.setRenderHint(QPainter.SmoothPixmapTransform)
        # # 设置缩放锚点，即缩放中心，这里设置为鼠标所在位置
        # self.graphicsView.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        # # 设置缩放时的锚点，这里设置为鼠标所在位置
        # self.graphicsView.setResizeAnchor(QGraphicsView.AnchorUnderMouse)
        # # 设置滚轮缩放的步长
        # self.graphicsView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # self.graphicsView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # self.graphicsView.setDragMode(QGraphicsView.ScrollHandDrag)
        # self.graphicsView.setOptimizationFlag(QGraphicsView.DontAdjustForAntialiasing, True)
        # self.graphicsView.setOptimizationFlag(QGraphicsView.DontSavePainterState, True)
        # self.graphicsView.setRenderHint(QPainter.Antialiasing)
        # self.graphicsView.setRenderHint(QPainter.TextAntialiasing)

        # 设置允许使用鼠标滚轮缩放
        self.graphicsView.setRenderHint(QPainter.Antialiasing)
        self.graphicsView.setRenderHint(QPainter.SmoothPixmapTransform)
        self.graphicsView.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.graphicsView.setResizeAnchor(QGraphicsView.AnchorUnderMouse)
        # 设置滚动条
        # self.graphicsView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # self.graphicsView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.graphicsView.setDragMode(QGraphicsView.ScrollHandDrag)
        self.graphicsView.setOptimizationFlag(QGraphicsView.DontAdjustForAntialiasing, True)
        self.graphicsView.setOptimizationFlag(QGraphicsView.DontSavePainterState, True)
        self.graphicsView.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)
        self.graphicsView.setRenderHint(QPainter.HighQualityAntialiasing)
        self.graphicsView.setRenderHint(QPainter.TextAntialiasing)
        self.graphicsView.setRenderHint(QPainter.LosslessImageRendering)
        self.graphicsView.setRenderHint(QPainter.NonCosmeticDefaultPen)
        self.graphicsView.setInteractive(True)
        self.graphicsView.setMouseTracking(True)
    def wheelEvent(self, event):
        # 如果鼠标滚轮向上滚动，放大图片
        if event.angleDelta().y() > 0:
            self.graphicsView.scale(1.1, 1.1)
        else:
            self.graphicsView.scale(0.9, 0.9)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # QApplication.setStyle('Windows')
    mainPage = MainWindow()
    mainPage.show()
    sys.exit(app.exec_())
