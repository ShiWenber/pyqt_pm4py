"""
pyqt5 App for pm4py

author: boer
last edited: 2022-12-29
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction, qApp, QMenu, QFileDialog
from PyQt5.QtGui import QIcon
from shutil import copy
import pm4py
import os
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
        self.comboBox.addItems(Utils.get_all_filenames_in_dir("./data"))
        self.comboBox_2.addItems(["alpha_miner", "heuristics_miner", "alpha_miner_plus", "inductive_miner"])
        self.actionimport_xes.triggered.connect(self.pop_up_open_files_window)
        self.actionimport_csv.triggered.connect(self.pop_up_open_files_window)

        self.pushButton.clicked.connect(self.pm4py_process_mining)
    def pop_up_open_files_window(self):
        fileNames, fileType = QFileDialog.getOpenFileNames(self, "选取文件", "./", "All Files (*);;CSV Files (*.csv);;XES Fioles(*.xes)")

        for i in fileNames:
            copy(i, "./data")
        # 刷新下拉框
        self.comboBox.clear()
        self.comboBox.addItems(Utils.get_all_filenames_in_dir("./data"))
    
    def pm4py_process_mining(self):
        log_path = "./data/" + self.comboBox.currentText()
        log = None
        # 读取日志
        if (log_path.endswith(".csv")):
            log = pm4py.read.read_ocel_csv(log_path)
        else: 
            log = pm4py.read_xes(log_path)

        # 选择算法
        algorithm = self.comboBox_2.currentText()
        process_model = None
        if algorithm == "alpha_miner":
            process_model = pm4py.discover_petri_net_alpha(log)
        elif algorithm == "heuristics_miner":
            process_model = pm4py.discover_heuristics_net(log) 
        elif algorithm == "alpha_miner_plus":
            process_model = pm4py.discover_petri_net_alpha_plus(log)
        elif algorithm == "inductive_miner":
            process_model = pm4py.discover_petri_net_inductive(log)
        else:
            return
        # 将模型导出为图片
        gviz = pm4py.visualization.petri_net.visualizer.apply(process_model)
        # 保存图片
        gviz.save("./res/" + algorithm + ".png")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # QApplication.setStyle('Windows')
    mainPage = MainWindow()
    mainPage.show()
    sys.exit(app.exec_())
