#!usr/bin/env python
# coding=utf-8
# Author: zhezhiyong@163.com
# Created: 2016年02月24日 24:14:40
# 编辑器：pycharm5.0.2，python版本：2.7.10
"""
# TODO(purpose): 
"""

import ctypes
import sys
from PyQt4 import QtGui, QtCore
from demoEngine import MainEngine
# from demoUi import *
from ui_order import Ui_Form
from eventEngine import *
import time

class Ui(QtGui.QWidget, Ui_Form):
    signalLog = QtCore.pyqtSignal(type(Event()))

    def __init__(self, eventEngine, mainEngine):
        super(Ui, self).__init__(None)
        self.setupUi(self)
        self.__eventEngine = eventEngine
        self.__mainEngine = mainEngine
        self.registerEvent()

    def registerEvent(self):
        """"""
        self.signalLog.connect(self.updateLog)
        self.__eventEngine.register(EVENT_LOG, self.signalLog.emit)

    # def updateLog(self, event):
    #     """"""
    #     log = event.dict_['log']
    #     self.bar.showMessage(log)
    def updateLog(self, event):
        """更新日志"""
        # 获取当前时间和日志内容
        t = time.strftime('%H:%M:%S',time.localtime(time.time()))
        log = event.dict_['log']
        # 在表格最上方插入一行
        self.tableWidget.insertRow(0)

        # 创建单元格
        cellTime = QtGui.QTableWidgetItem(t)
        cellLog = QtGui.QTableWidgetItem(log)

        # 将单元格插入表格
        self.tableWidget.setItem(0, 0, cellTime)
        self.tableWidget.setItem(0, 1, cellLog)

    def btn_send_order(self):
        print 'btn_send_order'
        event = Event(type_=EVENT_LOG)
        log = u'查询合约信息'
        event.dict_['log'] = log
        self.__eventEngine.put(event)
        pass


# ----------------------------------------------------------------------
def main():
    """主程序入口"""
    # ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('vn.py demo')  # win7以下请注释掉该行

    app = QtGui.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('vnpy.ico'))

    me = MainEngine()
    mw = Ui(me.ee, me)
    mw.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    import sys
    reload(sys)
    sys.setdefaultencoding( "utf-8" )
    main()
