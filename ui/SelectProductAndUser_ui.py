# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SelectProductAndUser.ui'
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

class Ui_SelectProductAndUser(object):
    def setupUi(self, SelectProductAndUser):
        SelectProductAndUser.setObjectName(_fromUtf8("SelectProductAndUser"))
        SelectProductAndUser.resize(318, 139)
        self.label = QtGui.QLabel(SelectProductAndUser)
        self.label.setGeometry(QtCore.QRect(40, 20, 101, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(SelectProductAndUser)
        self.label_2.setGeometry(QtCore.QRect(180, 20, 111, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.l_connectionInfo = QtGui.QLabel(SelectProductAndUser)
        self.l_connectionInfo.setGeometry(QtCore.QRect(60, 140, 201, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Agency FB"))
        self.l_connectionInfo.setFont(font)
        self.l_connectionInfo.setText(_fromUtf8(""))
        self.l_connectionInfo.setObjectName(_fromUtf8("l_connectionInfo"))
        self.pb_enter = QtGui.QPushButton(SelectProductAndUser)
        self.pb_enter.setGeometry(QtCore.QRect(60, 100, 75, 23))
        self.pb_enter.setObjectName(_fromUtf8("pb_enter"))
        self.pb_cancel = QtGui.QPushButton(SelectProductAndUser)
        self.pb_cancel.setGeometry(QtCore.QRect(190, 100, 75, 23))
        self.pb_cancel.setObjectName(_fromUtf8("pb_cancel"))
        self.ComB_Product = QtGui.QComboBox(SelectProductAndUser)
        self.ComB_Product.setGeometry(QtCore.QRect(40, 50, 101, 22))
        self.ComB_Product.setObjectName(_fromUtf8("ComB_Product"))
        self.ComB_User = QtGui.QComboBox(SelectProductAndUser)
        self.ComB_User.setGeometry(QtCore.QRect(180, 50, 101, 22))
        self.ComB_User.setObjectName(_fromUtf8("ComB_User"))

        self.retranslateUi(SelectProductAndUser)
        QtCore.QObject.connect(self.pb_cancel, QtCore.SIGNAL(_fromUtf8("clicked()")), SelectProductAndUser.close)
        QtCore.QMetaObject.connectSlotsByName(SelectProductAndUser)

    def retranslateUi(self, SelectProductAndUser):
        SelectProductAndUser.setWindowTitle(_translate("SelectProductAndUser", "选择产品管理组和账户", None))
        self.label.setText(_translate("SelectProductAndUser", "选择产品管理组", None))
        self.label_2.setText(_translate("SelectProductAndUser", "选择产品账户", None))
        self.pb_enter.setText(_translate("SelectProductAndUser", "确定", None))
        self.pb_cancel.setText(_translate("SelectProductAndUser", "取消", None))

