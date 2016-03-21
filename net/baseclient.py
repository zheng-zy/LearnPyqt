#!/usr/bin/env python
# -*- coding: utf-8 -*-


""" a base client class
"""

import inspect
import struct
import socket
from util import utils
from pb import base_pb2, error_pb2
import time

from datatype import Sesstion
from PyQt4.QtCore import QThread


def get_current_function():
    return inspect.stack()[1][3]


# -----------------------------------------------------------------------------
class BaseClient(QThread):
    def __init__(self, addr, callback=None):
        QThread.__init__(self, None)
        self.addr = addr
        self.running = 1
        self.svr_sock = None
        self.sess = Sesstion(None, None)

        if callback is None:
            self.handler = self.package_handle
        else:
            self.handler = callback

        self.svr_sock = self.connect_server(self.addr)
        # self.after_connect(0)

    def connect_server(self, addr):
        i = 2
        while self.running:
            try:
                svr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                svr.connect(addr)
                self.sess.sock = svr
                print('%s connected' % (self.__class__))
                break
            except Exception, e:
                time.sleep(i)
                print('reconect to %s %s' % (str(addr), e))
                i = i * 2
                if i >= 32:
                    i = 2

        return svr

    def reconnect_server(self, err):
        print('rereconnect to %s err %d' % (str(self.addr), err))
        try:
            self.svr_sock.shutdown(socket.SHUT_RDWR)
        except:
            pass
        self.svr_sock.close()
        self.svr_sock = self.connect_server(self.addr)
        self.after_connect(err)

    def run(self):
        MAX_PACK = 1024 * 1024
        while self.running:
            status, packlen, pi = utils.recv_header2(
                    self.svr_sock, base_pb2.HEADER_SIZE)
            if error_pb2.SUCCESS != status:
                self.reconnect_server(1)
                continue

            if packlen < 0 or packlen > MAX_PACK:
                self.reconnect_server(2)
                continue

            pi.sess = self.sess
            # 获取包体 收全包体
            body = ''
            status, body = utils.recv_body(self.svr_sock, packlen)
            if error_pb2.SUCCESS != status:
                self.reconnect_server(3)
                continue
            self.handler(packlen, pi, body)

        self.svr_sock.shutdown(socket.SHUT_RDWR)
        self.svr_sock.close()

    def send_heartbeat(self, sysid):
        print 'send_heartbeat'
        fmt = ">iHHiiii"
        headbuffer = struct.pack(
                fmt, 0, sysid, base_pb2.CMD_HEARTBEAT_RESP, sysid,
                0, 0, 0)
        self.svr_sock.sendall(headbuffer)

    def send_package(self, pack):
        # print 'send_package'
        try:
            self.svr_sock.send(pack)
        except Exception, e:
            print('\033[31msomething wrong!!!! %s \033[0m' % (e))
            self.reconnect_server(10)
            self.svr_sock.send(pack)

    def stop_running(self):
        self.running = 0

    def after_connect(self, err):
        print('%s: Not: %s %s' % (self.__class__, get_current_function(), err))

    def package_handle(self, packlen, pi, body):
        print('%s: not implement f: %s' % (self, get_current_function()))


def whoami():
    import sys
    return sys._getframe(1).f_code.co_name
