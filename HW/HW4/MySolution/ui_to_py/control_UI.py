# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/control.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_control(object):
    def setupUi(self, control):
        control.setObjectName("control")
        control.resize(498, 307)
        self.centralwidget = QtWidgets.QWidget(control)
        self.centralwidget.setObjectName("centralwidget")
        self.red = QtWidgets.QLineEdit(self.centralwidget)
        self.red.setGeometry(QtCore.QRect(360, 60, 131, 31))
        self.red.setObjectName("red")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 60, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 0, 0);")
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(-7, -1, 511, 51))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.stop = QtWidgets.QPushButton(self.centralwidget)
        self.stop.setGeometry(QtCore.QRect(30, 220, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.stop.setFont(font)
        self.stop.setObjectName("stop")
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(350, 220, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.start.setFont(font)
        self.start.setObjectName("start")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 170, 0);")
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.yellow = QtWidgets.QLineEdit(self.centralwidget)
        self.yellow.setGeometry(QtCore.QRect(360, 110, 131, 31))
        self.yellow.setObjectName("yellow")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 160, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgb(85, 170, 0)")
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.green = QtWidgets.QLineEdit(self.centralwidget)
        self.green.setGeometry(QtCore.QRect(360, 160, 131, 31))
        self.green.setObjectName("green")
        control.setCentralWidget(self.centralwidget)

        self.retranslateUi(control)
        QtCore.QMetaObject.connectSlotsByName(control)

    def retranslateUi(self, control):
        _translate = QtCore.QCoreApplication.translate
        control.setWindowTitle(_translate("control", "MainWindow"))
        self.label.setText(_translate("control", "Set Red Duration"))
        self.label_2.setText(_translate("control", "Contorl Panel"))
        self.stop.setText(_translate("control", "stop"))
        self.start.setText(_translate("control", "start"))
        self.label_3.setText(_translate("control", "Set Yellow Duration"))
        self.label_4.setText(_translate("control", "Set Green Duration"))
