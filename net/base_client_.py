#!usr/bin/env python
# coding=utf-8
# Author: zhezhiyong@163.com
# Created: 2016年02月26日 26:16:41
# 编辑器：pycharm3.4，python版本：2.66
"""
# TODO(purpose): 
"""
from PyQt4.QtCore import QThread
import socket
import struct
from pb import error_pb2, base_pb2
from util import utils


class BaseClient(QThread):
    def __init__(self, parent=None):
        QThread.__init__(self, parent)
        self.exiting = False
        self.sock = None
        self.size = 24
        self.connect_socket(('192.168.15.34', 9991))

    def __del__(self):
        self.exiting = True

    def connect_socket(self, address):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(address)

    def send_pack(self, pack):
        self.sock.sendall(pack)

    def run(self):
        MAX_PACK = 1024 * 1024
        while True:
            status, packlen, sysid, cmd, rid = utils.recv_header(self.sock, base_pb2.HEADER_SIZE)

            if error_pb2.SUCCESS != status:
                break
            if packlen < 0 or packlen > MAX_PACK:
                print 'close connect error length', packlen
                break

            # 获取包体 收全包体
            body = ''
            status, body = utils.recv_body(self.sock, packlen)
            if error_pb2.SUCCESS != status:
                break
            print('cmd 0x[%x] sysid [%x]' % (cmd, sysid))
            self.mt_handle(cmd, rid, body)

    def mt_handle(self, cmd, rid, body):
        pass
