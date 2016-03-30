# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SetKeyboard.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(320, 437)
        self.tableWidget = QtGui.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 301, 381))
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(15)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(23)
        self.tableWidget.verticalHeader().setMinimumSectionSize(15)
        self.pb_accept = QtGui.QPushButton(Dialog)
        self.pb_accept.setGeometry(QtCore.QRect(50, 400, 75, 30))
        self.pb_accept.setObjectName(_fromUtf8("pb_accept"))
        self.pb_cancel = QtGui.QPushButton(Dialog)
        self.pb_cancel.setGeometry(QtCore.QRect(200, 400, 75, 30))
        self.pb_cancel.setObjectName(_fromUtf8("pb_cancel"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "自定义快捷键", None))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "1", None))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Dialog", "2", None))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Dialog", "3", None))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Dialog", "4", None))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("Dialog", "5", None))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("Dialog", "6", None))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("Dialog", "7", None))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("Dialog", "8", None))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("Dialog", "9", None))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("Dialog", "10", None))
        item = self.tableWidget.verticalHeaderItem(10)
        item.setText(_translate("Dialog", "11", None))
        item = self.tableWidget.verticalHeaderItem(11)
        item.setText(_translate("Dialog", "12", None))
        item = self.tableWidget.verticalHeaderItem(12)
        item.setText(_translate("Dialog", "13", None))
        item = self.tableWidget.verticalHeaderItem(13)
        item.setText(_translate("Dialog", "14", None))
        item = self.tableWidget.verticalHeaderItem(14)
        item.setText(_translate("Dialog", "15", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "交易子界面", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "自定义快捷键", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "快捷菜单名称", None))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pb_accept.setText(_translate("Dialog", "确定", None))
        self.pb_cancel.setText(_translate("Dialog", "取消", None))

