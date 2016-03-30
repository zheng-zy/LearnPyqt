# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ETFBasisCalcOne.ui'
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

class Ui_GroupBox(object):
    def setupUi(self, GroupBox):
        GroupBox.setObjectName(_fromUtf8("GroupBox"))
        GroupBox.resize(260, 31)
        GroupBox.setMinimumSize(QtCore.QSize(0, 30))
        GroupBox.setStyleSheet(_fromUtf8("QGroupBox {\n"
"    border: 1px solid rgb(30,144,255)\n"
"};"))
        GroupBox.setTitle(_fromUtf8(""))
        self.line = QtGui.QFrame(GroupBox)
        self.line.setGeometry(QtCore.QRect(60, 0, 16, 31))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(GroupBox)
        self.line_2.setGeometry(QtCore.QRect(150, 0, 20, 31))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.l_red1 = QtGui.QLabel(GroupBox)
        self.l_red1.setGeometry(QtCore.QRect(80, 0, 24, 16))
        self.l_red1.setObjectName(_fromUtf8("l_red1"))
        self.l_red = QtGui.QLabel(GroupBox)
        self.l_red.setGeometry(QtCore.QRect(110, 0, 41, 16))
        self.l_red.setObjectName(_fromUtf8("l_red"))
        self.l_sell1 = QtGui.QLabel(GroupBox)
        self.l_sell1.setGeometry(QtCore.QRect(170, 0, 30, 16))
        self.l_sell1.setObjectName(_fromUtf8("l_sell1"))
        self.l_sell = QtGui.QLabel(GroupBox)
        self.l_sell.setGeometry(QtCore.QRect(210, 0, 41, 16))
        self.l_sell.setObjectName(_fromUtf8("l_sell"))
        self.l_cre1 = QtGui.QLabel(GroupBox)
        self.l_cre1.setGeometry(QtCore.QRect(80, 10, 24, 21))
        self.l_cre1.setObjectName(_fromUtf8("l_cre1"))
        self.l_cre = QtGui.QLabel(GroupBox)
        self.l_cre.setGeometry(QtCore.QRect(110, 10, 41, 21))
        self.l_cre.setObjectName(_fromUtf8("l_cre"))
        self.l_buy1 = QtGui.QLabel(GroupBox)
        self.l_buy1.setGeometry(QtCore.QRect(170, 10, 24, 21))
        self.l_buy1.setObjectName(_fromUtf8("l_buy1"))
        self.l_buy = QtGui.QLabel(GroupBox)
        self.l_buy.setGeometry(QtCore.QRect(210, 10, 41, 21))
        self.l_buy.setObjectName(_fromUtf8("l_buy"))
        self.pb_code = QtGui.QPushButton(GroupBox)
        self.pb_code.setGeometry(QtCore.QRect(10, 5, 51, 21))
        self.pb_code.setCheckable(True)
        self.pb_code.setChecked(False)
        self.pb_code.setFlat(True)
        self.pb_code.setObjectName(_fromUtf8("pb_code"))

        self.retranslateUi(GroupBox)
        QtCore.QMetaObject.connectSlotsByName(GroupBox)

    def retranslateUi(self, GroupBox):
        GroupBox.setWindowTitle(_translate("GroupBox", "GroupBox", None))
        self.l_red1.setText(_translate("GroupBox", "red:", None))
        self.l_red.setText(_translate("GroupBox", "0.0", None))
        self.l_sell1.setText(_translate("GroupBox", "sell:", None))
        self.l_sell.setText(_translate("GroupBox", "0.0", None))
        self.l_cre1.setText(_translate("GroupBox", "cre:", None))
        self.l_cre.setText(_translate("GroupBox", "0.0", None))
        self.l_buy1.setText(_translate("GroupBox", "buy:", None))
        self.l_buy.setText(_translate("GroupBox", "0.0", None))
        self.pb_code.setText(_translate("GroupBox", "PushButton", None))

