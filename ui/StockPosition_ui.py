# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StockPosition.ui'
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
        DockWidget.resize(860, 65)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.cb_no_zero_position = QtGui.QCheckBox(self.dockWidgetContents)
        self.cb_no_zero_position.setObjectName(_fromUtf8("cb_no_zero_position"))
        self.horizontalLayout.addWidget(self.cb_no_zero_position)
        self.cb_only_etf_fund = QtGui.QCheckBox(self.dockWidgetContents)
        self.cb_only_etf_fund.setObjectName(_fromUtf8("cb_only_etf_fund"))
        self.horizontalLayout.addWidget(self.cb_only_etf_fund)
        self.rb_code = QtGui.QRadioButton(self.dockWidgetContents)
        self.rb_code.setChecked(True)
        self.rb_code.setObjectName(_fromUtf8("rb_code"))
        self.horizontalLayout.addWidget(self.rb_code)
        self.le_code_data = QtGui.QLineEdit(self.dockWidgetContents)
        self.le_code_data.setObjectName(_fromUtf8("le_code_data"))
        self.horizontalLayout.addWidget(self.le_code_data)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pb_search = QtGui.QPushButton(self.dockWidgetContents)
        self.pb_search.setObjectName(_fromUtf8("pb_search"))
        self.horizontalLayout.addWidget(self.pb_search)
        self.pb_export = QtGui.QPushButton(self.dockWidgetContents)
        self.pb_export.setObjectName(_fromUtf8("pb_export"))
        self.horizontalLayout.addWidget(self.pb_export)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        DockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget)
        QtCore.QMetaObject.connectSlotsByName(DockWidget)

    def retranslateUi(self, DockWidget):
        DockWidget.setWindowTitle(_translate("DockWidget", "现货持仓", None))
        self.cb_no_zero_position.setText(_translate("DockWidget", "不显示0持仓", None))
        self.cb_only_etf_fund.setText(_translate("DockWidget", "只显示ETF和基金", None))
        self.rb_code.setText(_translate("DockWidget", "证券代码筛选", None))
        self.pb_search.setText(_translate("DockWidget", "查询", None))
        self.pb_export.setText(_translate("DockWidget", "导出", None))

