# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OrderList.ui'
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
        DockWidget.resize(984, 93)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.l_variety = QtGui.QLabel(self.dockWidgetContents)
        self.l_variety.setObjectName(_fromUtf8("l_variety"))
        self.horizontalLayout_3.addWidget(self.l_variety)
        self.rb_variety_all = QtGui.QRadioButton(self.dockWidgetContents)
        self.rb_variety_all.setChecked(True)
        self.rb_variety_all.setObjectName(_fromUtf8("rb_variety_all"))
        self.buttonGroup = QtGui.QButtonGroup(DockWidget)
        self.buttonGroup.setObjectName(_fromUtf8("buttonGroup"))
        self.buttonGroup.addButton(self.rb_variety_all)
        self.horizontalLayout_3.addWidget(self.rb_variety_all)
        self.rb_variety_fund = QtGui.QRadioButton(self.dockWidgetContents)
        self.rb_variety_fund.setChecked(False)
        self.rb_variety_fund.setObjectName(_fromUtf8("rb_variety_fund"))
        self.buttonGroup.addButton(self.rb_variety_fund)
        self.horizontalLayout_3.addWidget(self.rb_variety_fund)
        self.rb_variety_stock = QtGui.QRadioButton(self.dockWidgetContents)
        self.rb_variety_stock.setChecked(False)
        self.rb_variety_stock.setObjectName(_fromUtf8("rb_variety_stock"))
        self.buttonGroup.addButton(self.rb_variety_stock)
        self.horizontalLayout_3.addWidget(self.rb_variety_stock)
        self.rb_variety_stockCode = QtGui.QRadioButton(self.dockWidgetContents)
        self.rb_variety_stockCode.setChecked(False)
        self.rb_variety_stockCode.setObjectName(_fromUtf8("rb_variety_stockCode"))
        self.buttonGroup.addButton(self.rb_variety_stockCode)
        self.horizontalLayout_3.addWidget(self.rb_variety_stockCode)
        self.le_search_code = QtGui.QLineEdit(self.dockWidgetContents)
        self.le_search_code.setObjectName(_fromUtf8("le_search_code"))
        self.horizontalLayout_3.addWidget(self.le_search_code)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.l_ip = QtGui.QLabel(self.dockWidgetContents)
        self.l_ip.setObjectName(_fromUtf8("l_ip"))
        self.horizontalLayout_3.addWidget(self.l_ip)
        self.le_search_ip = QtGui.QLineEdit(self.dockWidgetContents)
        self.le_search_ip.setObjectName(_fromUtf8("le_search_ip"))
        self.horizontalLayout_3.addWidget(self.le_search_ip)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pb_search = QtGui.QPushButton(self.dockWidgetContents)
        self.pb_search.setObjectName(_fromUtf8("pb_search"))
        self.horizontalLayout_2.addWidget(self.pb_search)
        self.pb_cancel = QtGui.QPushButton(self.dockWidgetContents)
        self.pb_cancel.setObjectName(_fromUtf8("pb_cancel"))
        self.horizontalLayout_2.addWidget(self.pb_cancel)
        self.pb_buyCancel = QtGui.QPushButton(self.dockWidgetContents)
        self.pb_buyCancel.setObjectName(_fromUtf8("pb_buyCancel"))
        self.horizontalLayout_2.addWidget(self.pb_buyCancel)
        self.pb_sellCancel = QtGui.QPushButton(self.dockWidgetContents)
        self.pb_sellCancel.setObjectName(_fromUtf8("pb_sellCancel"))
        self.horizontalLayout_2.addWidget(self.pb_sellCancel)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.l_buy_name = QtGui.QLabel(self.dockWidgetContents)
        self.l_buy_name.setObjectName(_fromUtf8("l_buy_name"))
        self.horizontalLayout_2.addWidget(self.l_buy_name)
        self.l_buy_money = QtGui.QLabel(self.dockWidgetContents)
        self.l_buy_money.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.l_buy_money.setObjectName(_fromUtf8("l_buy_money"))
        self.horizontalLayout_2.addWidget(self.l_buy_money)
        self.l_buy_yuan = QtGui.QLabel(self.dockWidgetContents)
        self.l_buy_yuan.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.l_buy_yuan.setObjectName(_fromUtf8("l_buy_yuan"))
        self.horizontalLayout_2.addWidget(self.l_buy_yuan)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.l_sell_name = QtGui.QLabel(self.dockWidgetContents)
        self.l_sell_name.setObjectName(_fromUtf8("l_sell_name"))
        self.horizontalLayout_2.addWidget(self.l_sell_name)
        self.l_sell_money = QtGui.QLabel(self.dockWidgetContents)
        self.l_sell_money.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.l_sell_money.setObjectName(_fromUtf8("l_sell_money"))
        self.horizontalLayout_2.addWidget(self.l_sell_money)
        self.l_sell_yuan = QtGui.QLabel(self.dockWidgetContents)
        self.l_sell_yuan.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.l_sell_yuan.setObjectName(_fromUtf8("l_sell_yuan"))
        self.horizontalLayout_2.addWidget(self.l_sell_yuan)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        DockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget)
        QtCore.QMetaObject.connectSlotsByName(DockWidget)

    def retranslateUi(self, DockWidget):
        DockWidget.setWindowTitle(_translate("DockWidget", "委托列表", None))
        self.l_variety.setText(_translate("DockWidget", "品种", None))
        self.rb_variety_all.setText(_translate("DockWidget", "全部", None))
        self.rb_variety_fund.setText(_translate("DockWidget", "基金", None))
        self.rb_variety_stock.setText(_translate("DockWidget", "股票", None))
        self.rb_variety_stockCode.setText(_translate("DockWidget", "证券代码", None))
        self.l_ip.setText(_translate("DockWidget", "终端IP：", None))
        self.pb_search.setText(_translate("DockWidget", "查询", None))
        self.pb_cancel.setText(_translate("DockWidget", "撤单", None))
        self.pb_buyCancel.setText(_translate("DockWidget", "买单全撤", None))
        self.pb_sellCancel.setText(_translate("DockWidget", "卖单全撤", None))
        self.l_buy_name.setText(_translate("DockWidget", "买单全金额：", None))
        self.l_buy_money.setText(_translate("DockWidget", "0.0", None))
        self.l_buy_yuan.setText(_translate("DockWidget", "元", None))
        self.l_sell_name.setText(_translate("DockWidget", "卖单全金额：", None))
        self.l_sell_money.setText(_translate("DockWidget", "0.0", None))
        self.l_sell_yuan.setText(_translate("DockWidget", "元", None))

