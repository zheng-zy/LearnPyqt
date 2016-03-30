# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ETFBasisCalc.ui'
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

class Ui_DockWidget(object):
    def setupUi(self, DockWidget):
        DockWidget.setObjectName(_fromUtf8("DockWidget"))
        DockWidget.resize(261, 65)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.cb_code = QtGui.QComboBox(self.dockWidgetContents)
        self.cb_code.setMaximumSize(QtCore.QSize(65, 16777215))
        self.cb_code.setObjectName(_fromUtf8("cb_code"))
        self.horizontalLayout.addWidget(self.cb_code)
        self.label = QtGui.QLabel(self.dockWidgetContents)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.le_code = QtGui.QLineEdit(self.dockWidgetContents)
        self.le_code.setObjectName(_fromUtf8("le_code"))
        self.horizontalLayout.addWidget(self.le_code)
        self.pb_add = QtGui.QPushButton(self.dockWidgetContents)
        self.pb_add.setMaximumSize(QtCore.QSize(40, 16777215))
        self.pb_add.setObjectName(_fromUtf8("pb_add"))
        self.horizontalLayout.addWidget(self.pb_add)
        self.pb_del = QtGui.QPushButton(self.dockWidgetContents)
        self.pb_del.setMaximumSize(QtCore.QSize(40, 16777215))
        self.pb_del.setObjectName(_fromUtf8("pb_del"))
        self.horizontalLayout.addWidget(self.pb_del)
        self.verticalLayout.addLayout(self.horizontalLayout)
        DockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget)
        QtCore.QMetaObject.connectSlotsByName(DockWidget)

    def retranslateUi(self, DockWidget):
        DockWidget.setWindowTitle(_translate("DockWidget", "ETF基差计算", None))
        self.label.setText(_translate("DockWidget", "品种", None))
        self.pb_add.setText(_translate("DockWidget", "添加", None))
        self.pb_del.setText(_translate("DockWidget", "删除", None))

