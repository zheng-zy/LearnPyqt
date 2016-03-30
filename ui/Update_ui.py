# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Update.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(561, 402)
        self.lw_info = QtGui.QListWidget(Form)
        self.lw_info.setGeometry(QtCore.QRect(20, 90, 521, 221))
        self.lw_info.setObjectName(_fromUtf8("lw_info"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 60, 61, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 131, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 330, 81, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.pbar_percent = QtGui.QProgressBar(Form)
        self.pbar_percent.setGeometry(QtCore.QRect(20, 360, 531, 23))
        self.pbar_percent.setProperty("value", 0)
        self.pbar_percent.setObjectName(_fromUtf8("pbar_percent"))
        self.l_ipport = QtGui.QLabel(Form)
        self.l_ipport.setGeometry(QtCore.QRect(150, 20, 151, 16))
        self.l_ipport.setText(_fromUtf8(""))
        self.l_ipport.setObjectName(_fromUtf8("l_ipport"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "MTClient升级检测", None))
        self.label.setText(_translate("Form", "升级详情：", None))
        self.label_2.setText(_translate("Form", "升级服务器配置信息：", None))
        self.label_3.setText(_translate("Form", "软件更新进度", None))

