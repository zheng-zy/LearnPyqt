# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FutureTrade.ui'
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
        DockWidget.resize(278, 375)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.pb_buy = QtGui.QPushButton(self.dockWidgetContents)
        self.pb_buy.setGeometry(QtCore.QRect(10, 260, 111, 81))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Shruti"))
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.pb_buy.setFont(font)
        self.pb_buy.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pb_buy.setStyleSheet(_fromUtf8("QPushButton {border: 2px solid #c9c9c9; background-color: rgb(255, 255, 255);border-radius: 8px; color:rgb(255,0,0);text-align:bottom }\n"
"QPushButton:pressed { background-color:#000000; }"))
        self.pb_buy.setObjectName(_fromUtf8("pb_buy"))
        self.l_buy_price = QtGui.QLabel(self.dockWidgetContents)
        self.l_buy_price.setGeometry(QtCore.QRect(20, 270, 91, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Shruti"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.l_buy_price.setFont(font)
        self.l_buy_price.setStyleSheet(_fromUtf8("QLabel { color:rgb(255,0,0)}"))
        self.l_buy_price.setAlignment(QtCore.Qt.AlignCenter)
        self.l_buy_price.setObjectName(_fromUtf8("l_buy_price"))
        self.line = QtGui.QFrame(self.dockWidgetContents)
        self.line.setGeometry(QtCore.QRect(20, 290, 91, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.pb_sell = QtGui.QPushButton(self.dockWidgetContents)
        self.pb_sell.setGeometry(QtCore.QRect(150, 260, 111, 81))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Shruti"))
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.pb_sell.setFont(font)
        self.pb_sell.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pb_sell.setStyleSheet(_fromUtf8("QPushButton {border: 2px solid #c9c9c9; background-color: rgb(255, 255, 255);border-radius: 8px; color:#32CD32;text-align:bottom }\n"
"QPushButton:pressed { background-color:#000000; }"))
        self.pb_sell.setObjectName(_fromUtf8("pb_sell"))
        self.line_2 = QtGui.QFrame(self.dockWidgetContents)
        self.line_2.setGeometry(QtCore.QRect(160, 290, 91, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.l_sell_price = QtGui.QLabel(self.dockWidgetContents)
        self.l_sell_price.setGeometry(QtCore.QRect(160, 270, 91, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Shruti"))
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.l_sell_price.setFont(font)
        self.l_sell_price.setStyleSheet(_fromUtf8("QLabel { color:#32CD32}"))
        self.l_sell_price.setAlignment(QtCore.Qt.AlignCenter)
        self.l_sell_price.setObjectName(_fromUtf8("l_sell_price"))
        self.label = QtGui.QLabel(self.dockWidgetContents)
        self.label.setGeometry(QtCore.QRect(20, 20, 84, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.rb_variety_if = QtGui.QRadioButton(self.dockWidgetContents)
        self.rb_variety_if.setGeometry(QtCore.QRect(110, 24, 35, 20))
        self.rb_variety_if.setChecked(True)
        self.rb_variety_if.setObjectName(_fromUtf8("rb_variety_if"))
        self.buttonGroup = QtGui.QButtonGroup(DockWidget)
        self.buttonGroup.setObjectName(_fromUtf8("buttonGroup"))
        self.buttonGroup.addButton(self.rb_variety_if)
        self.rb_variety_ih = QtGui.QRadioButton(self.dockWidgetContents)
        self.rb_variety_ih.setGeometry(QtCore.QRect(160, 24, 35, 20))
        self.rb_variety_ih.setObjectName(_fromUtf8("rb_variety_ih"))
        self.buttonGroup.addButton(self.rb_variety_ih)
        self.rb_variety_ic = QtGui.QRadioButton(self.dockWidgetContents)
        self.rb_variety_ic.setGeometry(QtCore.QRect(210, 24, 35, 20))
        self.rb_variety_ic.setObjectName(_fromUtf8("rb_variety_ic"))
        self.buttonGroup.addButton(self.rb_variety_ic)
        self.label_2 = QtGui.QLabel(self.dockWidgetContents)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 84, 50))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.le_future_code = QtGui.QLineEdit(self.dockWidgetContents)
        self.le_future_code.setGeometry(QtCore.QRect(110, 64, 133, 20))
        self.le_future_code.setText(_fromUtf8(""))
        self.le_future_code.setObjectName(_fromUtf8("le_future_code"))
        self.label_3 = QtGui.QLabel(self.dockWidgetContents)
        self.label_3.setGeometry(QtCore.QRect(20, 100, 84, 31))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.le_future_num = QtGui.QLineEdit(self.dockWidgetContents)
        self.le_future_num.setGeometry(QtCore.QRect(110, 105, 133, 20))
        self.le_future_num.setObjectName(_fromUtf8("le_future_num"))
        self.cb_future_price_type = QtGui.QComboBox(self.dockWidgetContents)
        self.cb_future_price_type.setGeometry(QtCore.QRect(110, 140, 131, 20))
        self.cb_future_price_type.setObjectName(_fromUtf8("cb_future_price_type"))
        self.cb_future_price_type.addItem(_fromUtf8(""))
        self.cb_future_price_type.addItem(_fromUtf8(""))
        self.cb_future_price_type.addItem(_fromUtf8(""))
        self.cb_future_price_type.addItem(_fromUtf8(""))
        self.label_5 = QtGui.QLabel(self.dockWidgetContents)
        self.label_5.setGeometry(QtCore.QRect(20, 140, 84, 20))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_4 = QtGui.QLabel(self.dockWidgetContents)
        self.label_4.setGeometry(QtCore.QRect(44, 180, 60, 31))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.le_limit_price = QtGui.QLineEdit(self.dockWidgetContents)
        self.le_limit_price.setEnabled(False)
        self.le_limit_price.setGeometry(QtCore.QRect(110, 185, 133, 20))
        self.le_limit_price.setReadOnly(False)
        self.le_limit_price.setObjectName(_fromUtf8("le_limit_price"))
        self.rb_open = QtGui.QRadioButton(self.dockWidgetContents)
        self.rb_open.setGeometry(QtCore.QRect(30, 220, 47, 16))
        self.rb_open.setChecked(True)
        self.rb_open.setObjectName(_fromUtf8("rb_open"))
        self.buttonGroup_2 = QtGui.QButtonGroup(DockWidget)
        self.buttonGroup_2.setObjectName(_fromUtf8("buttonGroup_2"))
        self.buttonGroup_2.addButton(self.rb_open)
        self.rb_close = QtGui.QRadioButton(self.dockWidgetContents)
        self.rb_close.setGeometry(QtCore.QRect(90, 220, 47, 16))
        self.rb_close.setObjectName(_fromUtf8("rb_close"))
        self.buttonGroup_2.addButton(self.rb_close)
        self.cb_auto = QtGui.QCheckBox(self.dockWidgetContents)
        self.cb_auto.setGeometry(QtCore.QRect(180, 220, 47, 16))
        self.cb_auto.setObjectName(_fromUtf8("cb_auto"))
        self.label_8 = QtGui.QLabel(self.dockWidgetContents)
        self.label_8.setGeometry(QtCore.QRect(250, 104, 41, 20))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        DockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget)
        QtCore.QMetaObject.connectSlotsByName(DockWidget)

    def retranslateUi(self, DockWidget):
        DockWidget.setWindowTitle(_translate("DockWidget", "期货买卖", None))
        self.pb_buy.setText(_translate("DockWidget", "买入", None))
        self.l_buy_price.setText(_translate("DockWidget", "0.0", None))
        self.pb_sell.setText(_translate("DockWidget", "卖出", None))
        self.l_sell_price.setText(_translate("DockWidget", "0.0", None))
        self.label.setText(_translate("DockWidget", "期货品种选择：", None))
        self.rb_variety_if.setText(_translate("DockWidget", "IF", None))
        self.rb_variety_ih.setText(_translate("DockWidget", "IH", None))
        self.rb_variety_ic.setText(_translate("DockWidget", "IC", None))
        self.label_2.setText(_translate("DockWidget", "期货合约代码：", None))
        self.label_3.setText(_translate("DockWidget", "期货合约数量：", None))
        self.cb_future_price_type.setItemText(0, _translate("DockWidget", "市价", None))
        self.cb_future_price_type.setItemText(1, _translate("DockWidget", "限价", None))
        self.cb_future_price_type.setItemText(2, _translate("DockWidget", "对手价超一", None))
        self.cb_future_price_type.setItemText(3, _translate("DockWidget", "对手价超五", None))
        self.label_5.setText(_translate("DockWidget", "期货价格类型：", None))
        self.label_4.setText(_translate("DockWidget", "限价价格：", None))
        self.rb_open.setText(_translate("DockWidget", "开仓", None))
        self.rb_close.setText(_translate("DockWidget", "平仓", None))
        self.cb_auto.setText(_translate("DockWidget", "自动", None))
        self.label_8.setText(_translate("DockWidget", "张", None))
