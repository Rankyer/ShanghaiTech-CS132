# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/query.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_query(object):
    def setupUi(self, query):
        query.setObjectName("query")
        query.resize(573, 333)
        self.centralwidget = QtWidgets.QWidget(query)
        self.centralwidget.setObjectName("centralwidget")
        self.current_account = QtWidgets.QLabel(self.centralwidget)
        self.current_account.setGeometry(QtCore.QRect(190, 30, 131, 21))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setBold(True)
        font.setWeight(75)
        self.current_account.setFont(font)
        self.current_account.setStyleSheet("background-color: rgb(220, 220, 220);")
        self.current_account.setObjectName("current_account")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 171, 61))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(170, 0, 0);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(40, 80, 491, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.return_to_main = QtWidgets.QPushButton(self.centralwidget)
        self.return_to_main.setGeometry(QtCore.QRect(370, 280, 161, 41))
        self.return_to_main.setObjectName("return_to_main")
        query.setCentralWidget(self.centralwidget)

        self.retranslateUi(query)
        QtCore.QMetaObject.connectSlotsByName(query)

    def retranslateUi(self, query):
        _translate = QtCore.QCoreApplication.translate
        query.setWindowTitle(_translate("query", "MainWindow"))
        self.current_account.setText(_translate("query", "TextLabel"))
        self.label_2.setText(_translate("query", "当前账户*"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("query", "账户余额"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("query", "交易类型"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("query", "交易金额"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("query", "交易时间"))
        self.return_to_main.setText(_translate("query", "返回主页"))
