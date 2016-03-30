# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
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

class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName(_fromUtf8("Login"))
        Login.resize(242, 143)
        self.l_ip = QtGui.QLabel(Login)
        self.l_ip.setGeometry(QtCore.QRect(30, 20, 71, 16))
        self.l_ip.setObjectName(_fromUtf8("l_ip"))
        self.l_passwd = QtGui.QLabel(Login)
        self.l_passwd.setGeometry(QtCore.QRect(60, 50, 31, 16))
        self.l_passwd.setObjectName(_fromUtf8("l_passwd"))
        self.le_ip = QtGui.QLineEdit(Login)
        self.le_ip.setGeometry(QtCore.QRect(100, 20, 113, 20))
        self.le_ip.setObjectName(_fromUtf8("le_ip"))
        self.le_passwd = QtGui.QLineEdit(Login)
        self.le_passwd.setGeometry(QtCore.QRect(100, 50, 113, 20))
        self.le_passwd.setEchoMode(QtGui.QLineEdit.Password)
        self.le_passwd.setObjectName(_fromUtf8("le_passwd"))
        self.cb_remember = QtGui.QCheckBox(Login)
        self.cb_remember.setGeometry(QtCore.QRect(70, 80, 121, 16))
        self.cb_remember.setChecked(True)
        self.cb_remember.setObjectName(_fromUtf8("cb_remember"))
        self.pb_login = QtGui.QPushButton(Login)
        self.pb_login.setGeometry(QtCore.QRect(30, 110, 75, 23))
        self.pb_login.setObjectName(_fromUtf8("pb_login"))
        self.pb_cancel = QtGui.QPushButton(Login)
        self.pb_cancel.setGeometry(QtCore.QRect(140, 110, 75, 23))
        self.pb_cancel.setObjectName(_fromUtf8("pb_cancel"))

        self.retranslateUi(Login)
        QtCore.QObject.connect(self.pb_cancel, QtCore.SIGNAL(_fromUtf8("clicked()")), Login.close)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        Login.setWindowTitle(_translate("Login", "登录", None))
        self.l_ip.setText(_translate("Login", "终端登录IP", None))
        self.l_passwd.setText(_translate("Login", "密码", None))
        self.cb_remember.setText(_translate("Login", "记住登录IP和密码", None))
        self.pb_login.setText(_translate("Login", "登录", None))
        self.pb_cancel.setText(_translate("Login", "取消", None))

