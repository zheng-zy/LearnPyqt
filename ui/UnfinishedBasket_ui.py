# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UnfinishedBasket.ui'
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
        Dialog.resize(525, 284)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.tv_unfinished_basket_list = QtGui.QTableWidget(Dialog)
        self.tv_unfinished_basket_list.setObjectName(_fromUtf8("tv_unfinished_basket_list"))
        self.tv_unfinished_basket_list.setColumnCount(7)
        self.tv_unfinished_basket_list.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tv_unfinished_basket_list.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tv_unfinished_basket_list.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tv_unfinished_basket_list.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tv_unfinished_basket_list.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tv_unfinished_basket_list.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tv_unfinished_basket_list.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tv_unfinished_basket_list.setHorizontalHeaderItem(6, item)
        self.tv_unfinished_basket_list.horizontalHeader().setDefaultSectionSize(70)
        self.tv_unfinished_basket_list.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.tv_unfinished_basket_list)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pb_choose = QtGui.QPushButton(Dialog)
        self.pb_choose.setObjectName(_fromUtf8("pb_choose"))
        self.horizontalLayout.addWidget(self.pb_choose)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pb_cancel = QtGui.QPushButton(Dialog)
        self.pb_cancel.setObjectName(_fromUtf8("pb_cancel"))
        self.horizontalLayout.addWidget(self.pb_cancel)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "未完成篮子", None))
        self.label.setText(_translate("Dialog", "选择未完成篮子：", None))
        item = self.tv_unfinished_basket_list.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "选择", None))
        item = self.tv_unfinished_basket_list.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "篮子代码", None))
        item = self.tv_unfinished_basket_list.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "篮子数量", None))
        item = self.tv_unfinished_basket_list.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "买卖方向", None))
        item = self.tv_unfinished_basket_list.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "已成金额", None))
        item = self.tv_unfinished_basket_list.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "完成百分比", None))
        item = self.tv_unfinished_basket_list.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "策略ID", None))
        self.pb_choose.setText(_translate("Dialog", "选择", None))
        self.pb_cancel.setText(_translate("Dialog", "取消", None))

