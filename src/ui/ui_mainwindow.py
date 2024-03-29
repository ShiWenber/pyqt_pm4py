# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(833, 720)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(40, 0))
        self.label.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.horizontalLayout.addWidget(self.comboBox_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton, 0, QtCore.Qt.AlignHCenter)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.verticalLayout)
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.graphicsView)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 833, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuimport = QtWidgets.QMenu(self.menuFile)
        self.menuimport.setObjectName("menuimport")
        self.menuexport = QtWidgets.QMenu(self.menuFile)
        self.menuexport.setObjectName("menuexport")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionimport_csv = QtWidgets.QAction(MainWindow)
        self.actionimport_csv.setObjectName("actionimport_csv")
        self.actionimport_xes = QtWidgets.QAction(MainWindow)
        self.actionimport_xes.setObjectName("actionimport_xes")
        self.actionexport_as_png = QtWidgets.QAction(MainWindow)
        self.actionexport_as_png.setObjectName("actionexport_as_png")
        self.actionopen_data_dir = QtWidgets.QAction(MainWindow)
        self.actionopen_data_dir.setObjectName("actionopen_data_dir")
        self.menuimport.addAction(self.actionimport_csv)
        self.menuimport.addAction(self.actionimport_xes)
        self.menuimport.addAction(self.actionopen_data_dir)
        self.menuexport.addAction(self.actionexport_as_png)
        self.menuFile.addAction(self.menuimport.menuAction())
        self.menuFile.addAction(self.menuexport.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "日志文件"))
        self.label_2.setText(_translate("MainWindow", "挖掘算法"))
        self.pushButton.setText(_translate("MainWindow", "挖掘"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuimport.setTitle(_translate("MainWindow", "import"))
        self.menuexport.setTitle(_translate("MainWindow", "export"))
        self.actionimport_csv.setText(_translate("MainWindow", "import csv"))
        self.actionimport_xes.setText(_translate("MainWindow", "import xes"))
        self.actionexport_as_png.setText(_translate("MainWindow", "export as png"))
        self.actionopen_data_dir.setText(_translate("MainWindow", "open data dir"))
