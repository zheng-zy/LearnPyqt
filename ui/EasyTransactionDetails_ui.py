# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EasyTransactionDetails.ui'
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

class Ui_d_easyTransactionDetails(object):
    def setupUi(self, d_easyTransactionDetails):
        d_easyTransactionDetails.setObjectName(_fromUtf8("d_easyTransactionDetails"))
        d_easyTransactionDetails.resize(684, 65)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.l_variety = QtGui.QLabel(self.dockWidgetContents)
        self.l_variety.setObjectName(_fromUtf8("l_variety"))
        self.horizontalLayout_3.addWidget(self.l_variety)
        self.rb_tradeTerminal_all = QtGui.QRadioButton(self.dockWidgetContents)
        self.rb_tradeTerminal_all.setChecked(True)
        self.rb_tradeTerminal_all.setObjectName(_fromUtf8("rb_tradeTerminal_all"))
        self.buttonGroup = QtGui.QButtonGroup(d_easyTransactionDetails)
        self.buttonGroup.setObjectName(_fromUtf8("buttonGroup"))
        self.buttonGroup.addButton(self.rb_tradeTerminal_all)
        self.horizontalLayout_3.addWidget(self.rb_tradeTerminal_all)
        self.rb_variety_stock = QtGui.QRadioButton(self.dockWidgetContents)
        self.rb_variety_stock.setChecked(False)
        self.rb_variety_stock.setObjectName(_fromUtf8("rb_variety_stock"))
        self.buttonGroup.addButton(self.rb_variety_stock)
        self.horizontalLayout_3.addWidget(self.rb_variety_stock)
        self.rb_variety_other = QtGui.QRadioButton(self.dockWidgetContents)
        self.rb_variety_other.setChecked(False)
        self.rb_variety_other.setObjectName(_fromUtf8("rb_variety_other"))
        self.buttonGroup.addButton(self.rb_variety_other)
        self.horizontalLayout_3.addWidget(self.rb_variety_other)
        spacerItem = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.l_tradeTerminal = QtGui.QLabel(self.dockWidgetContents)
        self.l_tradeTerminal.setObjectName(_fromUtf8("l_tradeTerminal"))
        self.horizontalLayout_3.addWidget(self.l_tradeTerminal)
        self.rb_variety_all = QtGui.QRadioButton(self.dockWidgetContents)
        self.rb_variety_all.setChecked(True)
        self.rb_variety_all.setObjectName(_fromUtf8("rb_variety_all"))
        self.buttonGroup_2 = QtGui.QButtonGroup(d_easyTransactionDetails)
        self.buttonGroup_2.setObjectName(_fromUtf8("buttonGroup_2"))
        self.buttonGroup_2.addButton(self.rb_variety_all)
        self.horizontalLayout_3.addWidget(self.rb_variety_all)
        self.rb_tradeTerminal_self = QtGui.QRadioButton(self.dockWidgetContents)
        self.rb_tradeTerminal_self.setChecked(False)
        self.rb_tradeTerminal_self.setObjectName(_fromUtf8("rb_tradeTerminal_self"))
        self.buttonGroup_2.addButton(self.rb_tradeTerminal_self)
        self.horizontalLayout_3.addWidget(self.rb_tradeTerminal_self)
        self.rb_tradeTerminal_ip = QtGui.QRadioButton(self.dockWidgetContents)
        self.rb_tradeTerminal_ip.setChecked(False)
        self.rb_tradeTerminal_ip.setObjectName(_fromUtf8("rb_tradeTerminal_ip"))
        self.buttonGroup_2.addButton(self.rb_tradeTerminal_ip)
        self.horizontalLayout_3.addWidget(self.rb_tradeTerminal_ip)
        self.le_search = QtGui.QLineEdit(self.dockWidgetContents)
        self.le_search.setObjectName(_fromUtf8("le_search"))
        self.horizontalLayout_3.addWidget(self.le_search)
        self.pb_search = QtGui.QPushButton(self.dockWidgetContents)
        self.pb_search.setObjectName(_fromUtf8("pb_search"))
        self.horizontalLayout_3.addWidget(self.pb_search)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        d_easyTransactionDetails.setWidget(self.dockWidgetContents)

        self.retranslateUi(d_easyTransactionDetails)
        QtCore.QMetaObject.connectSlotsByName(d_easyTransactionDetails)

    def retranslateUi(self, d_easyTransactionDetails):
        d_easyTransactionDetails.setWindowTitle(_translate("d_easyTransactionDetails", "简版成交明细", None))
        self.l_variety.setText(_translate("d_easyTransactionDetails", "品种", None))
        self.rb_tradeTerminal_all.setAccessibleName(_translate("d_easyTransactionDetails", "pingzhong", None))
        self.rb_tradeTerminal_all.setText(_translate("d_easyTransactionDetails", "全部", None))
        self.rb_variety_stock.setAccessibleName(_translate("d_easyTransactionDetails", "pingzhong", None))
        self.rb_variety_stock.setText(_translate("d_easyTransactionDetails", "股票", None))
        self.rb_variety_other.setAccessibleName(_translate("d_easyTransactionDetails", "pingzhong", None))
        self.rb_variety_other.setText(_translate("d_easyTransactionDetails", "其他", None))
        self.l_tradeTerminal.setText(_translate("d_easyTransactionDetails", "交易终端", None))
        self.rb_variety_all.setAccessibleName(_translate("d_easyTransactionDetails", "zhongduan", None))
        self.rb_variety_all.setText(_translate("d_easyTransactionDetails", "全部", None))
        self.rb_tradeTerminal_self.setAccessibleName(_translate("d_easyTransactionDetails", "zhongduan", None))
        self.rb_tradeTerminal_self.setText(_translate("d_easyTransactionDetails", "自己", None))
        self.rb_tradeTerminal_ip.setAccessibleName(_translate("d_easyTransactionDetails", "zhongduan", None))
        self.rb_tradeTerminal_ip.setText(_translate("d_easyTransactionDetails", "终端IP", None))
        self.pb_search.setText(_translate("d_easyTransactionDetails", "查询", None))

