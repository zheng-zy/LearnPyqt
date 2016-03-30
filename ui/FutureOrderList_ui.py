# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FutureOrderList.ui'
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
        DockWidget.resize(866, 65)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pb_cancel = QtGui.QPushButton(self.dockWidgetContents)
        self.pb_cancel.setObjectName(_fromUtf8("pb_cancel"))
        self.horizontalLayout.addWidget(self.pb_cancel)
        self.pb_cancel_all = QtGui.QPushButton(self.dockWidgetContents)
        self.pb_cancel_all.setObjectName(_fromUtf8("pb_cancel_all"))
        self.horizontalLayout.addWidget(self.pb_cancel_all)
        spacerItem = QtGui.QSpacerItem(538, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pb_export = QtGui.QPushButton(self.dockWidgetContents)
        self.pb_export.setObjectName(_fromUtf8("pb_export"))
        self.horizontalLayout.addWidget(self.pb_export)
        self.verticalLayout.addLayout(self.horizontalLayout)
        DockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget)
        QtCore.QMetaObject.connectSlotsByName(DockWidget)

    def retranslateUi(self, DockWidget):
        DockWidget.setWindowTitle(_translate("DockWidget", "期货委托价格", None))
        self.pb_cancel.setText(_translate("DockWidget", "撤单", None))
        self.pb_cancel_all.setText(_translate("DockWidget", "全部撤单", None))
        self.pb_export.setText(_translate("DockWidget", "导出", None))

