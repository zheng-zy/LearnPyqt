#!usr/bin/env python
# coding=utf-8
# Author: zhezhiyong@163.com
# Created: 2016年02月26日 26:15:09
# 编辑器：pycharm3.4，python版本：2.66
"""
# TODO(purpose): 
"""
import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import QThread
import socket
import uuid
import struct
import base_pb2, ot_pb2,stock_trade_pb2, trade_db_model_pb2

def make_package(sysid, cmd, rid, pack):
    fmt = ">iHH16s"
    head = struct.pack(fmt, pack.ByteSize(), sysid, cmd, rid.get_bytes())
    snddata = head + pack.SerializeToString()
    return snddata
class UiThread(QThread):
    def __init__(self, parent=None):
        QThread.__init__(self, parent)
        self.exiting = False
        self.sock = None
        self.connect_socket()
        self.login()

    def __del__(self):
        self.exiting = True

    def connect_socket(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(('192.168.15.34', 9991))

    def login(self):
        fmt = ">iHH16s"
        seq16 = uuid.uuid1()
        login = base_pb2.LoginReq()
        login.type = base_pb2.MANUAL_TRADE
        login.trader_id = 'tid'
        print 'login.version: [%s]' % login.version
        login.version = base_pb2.MAJOR << 16 or base_pb2.MINOR
        headbuffer = struct.pack(fmt, login.ByteSize(), base_pb2.SYS_MTC,
                                 base_pb2.CMD_LOGIN_REQ, seq16.get_bytes())
        sentdata = headbuffer + login.SerializeToString()
        self.send_msg(sentdata)

    def send_single_order(sess, code='502048', direction=base_pb2.POLICY_DIRECTION_POSITIVE, qty=200,price_level=base_pb2.S_1,price=10000, type=base_pb2.CMD_SINGLE_ORDER_REQ):
        sng_order = ot_pb2.StockPolicy()
        sng_order.base_param.direction = direction
        sng_order.base_param.trader_id = 'PH1'
        sng_order.base_param.trader_ip = '192.168.15.34'
        sng_order.base_param.logic_type = 'null'
        sng_order.code = code
        sng_order.volume = qty
        sng_order.price_level = base_pb2.S_1
        sng_order.price = price
        # 0表示不启用
        sng_order.reorder_interval = 0
        rid = uuid.uuid1()
        snddata = make_package(base_pb2.SYS_STOCK, type, rid, sng_order)
        sess.sock.send(snddata)

    def send_msg(self, msg):
        self.sock.sendall(msg)

    def run(self):
        while 1:
            data = self.sock.recv(1024)
            print data


if __name__ == "__main__":
    import time

    app = QtGui.QApplication(sys.argv)
    t = UiThread(None)
    t.start()
    time.sleep(1)
    t.send_single_order()
    print t.isFinished()
    app.exec_()
