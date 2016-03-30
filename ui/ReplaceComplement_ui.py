# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ReplaceComplement.ui'
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
        Dialog.resize(471, 334)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.l_qksz_name = QtGui.QLabel(Dialog)
        self.l_qksz_name.setObjectName(_fromUtf8("l_qksz_name"))
        self.horizontalLayout.addWidget(self.l_qksz_name)
        self.l_qksz_data = QtGui.QLabel(Dialog)
        self.l_qksz_data.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.l_qksz_data.setObjectName(_fromUtf8("l_qksz_data"))
        self.horizontalLayout.addWidget(self.l_qksz_data)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.l_yxsz_name = QtGui.QLabel(Dialog)
        self.l_yxsz_name.setObjectName(_fromUtf8("l_yxsz_name"))
        self.horizontalLayout.addWidget(self.l_yxsz_name)
        self.l_yxsz_data = QtGui.QLabel(Dialog)
        self.l_yxsz_data.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.l_yxsz_data.setObjectName(_fromUtf8("l_yxsz_data"))
        self.horizontalLayout.addWidget(self.l_yxsz_data)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tv_data_list = QtGui.QTableWidget(Dialog)
        self.tv_data_list.setObjectName(_fromUtf8("tv_data_list"))
        self.tv_data_list.setColumnCount(7)
        self.tv_data_list.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tv_data_list.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tv_data_list.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tv_data_list.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tv_data_list.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tv_data_list.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tv_data_list.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tv_data_list.setHorizontalHeaderItem(6, item)
        self.tv_data_list.horizontalHeader().setDefaultSectionSize(64)
        self.verticalLayout.addWidget(self.tv_data_list)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.pb_plbz = QtGui.QPushButton(Dialog)
        self.pb_plbz.setObjectName(_fromUtf8("pb_plbz"))
        self.horizontalLayout_2.addWidget(self.pb_plbz)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.pb_cancel = QtGui.QPushButton(Dialog)
        self.pb_cancel.setObjectName(_fromUtf8("pb_cancel"))
        self.horizontalLayout_2.addWidget(self.pb_cancel)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "替代补足", None))
        self.l_qksz_name.setText(_translate("Dialog", "现金替代上限缺口市值：", None))
        self.l_qksz_data.setText(_translate("Dialog", "12,561.12", None))
        self.l_yxsz_name.setText(_translate("Dialog", "替代补足已选市值：", None))
        self.l_yxsz_data.setText(_translate("Dialog", "12,561.12", None))
        item = self.tv_data_list.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "勾选", None))
        item = self.tv_data_list.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "序号", None))
        item = self.tv_data_list.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "股票代码", None))
        item = self.tv_data_list.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "股票名称", None))
        item = self.tv_data_list.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "股票状态", None))
        item = self.tv_data_list.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "缺口数量", None))
        item = self.tv_data_list.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "缺口市值", None))
        self.pb_plbz.setText(_translate("Dialog", "批量补足", None))
        self.pb_cancel.setText(_translate("Dialog", "取消", None))

