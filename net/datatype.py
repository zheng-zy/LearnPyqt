#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" global data type define
"""

__author__ = 'qinjing'
import uuid

class package_info(object):
    __slots__ = ('cmd', 'rid', 'pack', 'sess', 'opr', 'sock')

    def __str__(self):
        return ('cmd:0x%x uuid:%s sock:%s sess %s\npack:%s' %
                (self.cmd, self.rid, self.sess, self.sess, self.pack))

    def __init__(self, cmd, rid, pack=None, sess=None):
        self.cmd = cmd
        self.rid = uuid.UUID(bytes=rid)
        self.opr = 0
        self.pack = pack
        if sess is not None:
            assert isinstance(sess, Sesstion)
            self.sess = sess
        if (sess is not None):
            self.sock = sess.sock


class Sesstion(object):
    # tid 交易员id：trade_id
    # sock 通信实例
    def __init__(self, tid, sock):
        self.tid = tid
        self.sock = sock
        self.login = -1
        self.closed = 0

    def __str__(self):
        return 'tid:%s sock:%s' % (self.tid, self.sock)

    def close(self):
        self.closed = 1
        self.sock.close()

    def send_package(self, pack):
        if 0 == self.closed:
            try:
                self.sock.send(pack)
            except Exception, e:
                print('\033[31msomething wrong!!!! %s \033[0m' % (e))
