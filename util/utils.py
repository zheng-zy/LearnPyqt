#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
helper function
"""

import struct
import time
from pb import error_pb2
from net.datatype import package_info


# --------------------------------------------------------------------------
def recv_header(sock, size):
    header = ''
    while len(header) < size:
        hpdata = sock.recv(size - len(header))
        if not hpdata:
            print 'no header'
            break
        header += hpdata

    if len(header) == size:
        fmt = '>iHH16s'
        blen, sysid, cmd, rid = struct.unpack(fmt, header)
        return error_pb2.SUCCESS, blen, sysid, cmd, rid
    else:
        return error_pb2.ERROR_DISCONNECT, 0, 0, 0, 0


# -----------------------------------------------------------------------------
def recv_body(sock, size):
    body = ''
    while len(body) < size:
        bpdata = sock.recv(size - len(body))
        if not bpdata:
            print 'no body'
            break
        body += bpdata

    if len(body) == size:
        return error_pb2.SUCCESS, body
    else:
        return error_pb2.ERROR_DISCONNECT, body


def recv_header2(sock, size):
    header = ''
    while len(header) < size:
        try:
            hpdata = sock.recv(size - len(header))
        except Exception, e:
            print('except %s' % (e))
            break
        if not hpdata:
            time.sleep(0)
            print 'no header'
            break
        header += hpdata

    if len(header) == size:
        fmt = '>iHH16s'
        blen, sysid, cmd, rid = struct.unpack(fmt, header)
        pi = package_info(cmd, rid)
        return error_pb2.SUCCESS, blen, pi
    else:
        return error_pb2.ERROR_DISCONNECT, 0, None
