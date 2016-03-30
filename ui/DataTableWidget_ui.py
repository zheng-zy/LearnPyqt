# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DataTableWidget.ui'
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
        Form.resize(656, 300)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tb = QtGui.QTableWidget(Form)
        self.tb.setObjectName(_fromUtf8("tb"))
        self.tb.setColumnCount(0)
        self.tb.setRowCount(0)
        self.verticalLayout.addWidget(self.tb)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.l_pageInfo = QtGui.QLabel(Form)
        self.l_pageInfo.setObjectName(_fromUtf8("l_pageInfo"))
        self.horizontalLayout_2.addWidget(self.l_pageInfo)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pb_firstPage = QtGui.QPushButton(Form)
        self.pb_firstPage.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pb_firstPage.setObjectName(_fromUtf8("pb_firstPage"))
        self.horizontalLayout_2.addWidget(self.pb_firstPage)
        self.pb_prePage = QtGui.QPushButton(Form)
        self.pb_prePage.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pb_prePage.setObjectName(_fromUtf8("pb_prePage"))
        self.horizontalLayout_2.addWidget(self.pb_prePage)
        self.le_pageNumber = QtGui.QLineEdit(Form)
        self.le_pageNumber.setMaximumSize(QtCore.QSize(60, 16777215))
        self.le_pageNumber.setMaxLength(32769)
        self.le_pageNumber.setAlignment(QtCore.Qt.AlignCenter)
        self.le_pageNumber.setObjectName(_fromUtf8("le_pageNumber"))
        self.horizontalLayout_2.addWidget(self.le_pageNumber)
        self.pb_gotoPage = QtGui.QPushButton(Form)
        self.pb_gotoPage.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pb_gotoPage.setObjectName(_fromUtf8("pb_gotoPage"))
        self.horizontalLayout_2.addWidget(self.pb_gotoPage)
        self.pb_nextPage = QtGui.QPushButton(Form)
        self.pb_nextPage.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pb_nextPage.setObjectName(_fromUtf8("pb_nextPage"))
        self.horizontalLayout_2.addWidget(self.pb_nextPage)
        self.pb_lastPage = QtGui.QPushButton(Form)
        self.pb_lastPage.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pb_lastPage.setObjectName(_fromUtf8("pb_lastPage"))
        self.horizontalLayout_2.addWidget(self.pb_lastPage)
        self.cb_auto = QtGui.QCheckBox(Form)
        self.cb_auto.setObjectName(_fromUtf8("cb_auto"))
        self.horizontalLayout_2.addWidget(self.cb_auto)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.l_pageInfo.setText(_translate("Form", "总计0条，当前第0页/共0页", None))
        self.pb_firstPage.setText(_translate("Form", "首页", None))
        self.pb_prePage.setText(_translate("Form", "上一页", None))
        self.le_pageNumber.setText(_translate("Form", "1", None))
        self.pb_gotoPage.setText(_translate("Form", "跳转", None))
        self.pb_nextPage.setText(_translate("Form", "下一页", None))
        self.pb_lastPage.setText(_translate("Form", "末页", None))
        self.cb_auto.setText(_translate("Form", "自动滚屏", None))

