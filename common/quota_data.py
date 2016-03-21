#!usr/bin/env python
# coding=utf-8
# Author: zhezhiyong@163.com
# Created: 2016年02月23日 23:16:02
# 编辑器：pycharm5.0.2，python版本：2.7.10
"""
# TODO(purpose): 行情数据存储
"""

import gevent
from pb import base_pb2


class QuotaData(object):
    # 分级基金基础数据  code:info
    __structured_fund_info_datas = {}
    # 现货股票市场     code:market
    __stock_market_quotas = {}
    # 股票当日编号     code:idnum
    __code_idnum = {}
    # 现货实时行情     idnum:info
    __stock_real_time_quotas = {}

    def __init__(self):
        pass

    @classmethod
    def add_structured_fund_info(cls, key, data):
        cls.__structured_fund_info_datas[key] = data
        pass

    @classmethod
    def get_structured_fund_info(cls, key):
        return cls.__structured_fund_info_datas.get(key)

    @classmethod
    def add_stock_market_quotas(cls, key, data):
        cls.__stock_market_quotas[key] = data
        pass

    @classmethod
    def get_stock_market_quotas(cls, key):
        return cls.__stock_market_quotas.get(key)

    @classmethod
    def add_code_idnum(cls, key, data):
        cls.__code_idnum[key] = data
        pass

    @classmethod
    def get_code_idnum(cls, key):
        return cls.__code_idnum.get(key)

    @classmethod
    def add_stock_real_time_quotas(cls, key, data):
        cls.__stock_real_time_quotas[key] = data
        pass

    @classmethod
    def get_stock_real_time_quotas(cls, key):
        return cls.__stock_real_time_quotas.get(key)

    @classmethod
    def get_real_time_md(cls, key):
        return cls.get_stock_real_time_quotas(cls.get_code_idnum(key))

    @classmethod
    def get_price(cls, code, pl, bs_flag):
        price = 0
        i = 0
        md = cls.get_real_time_md(code)
        while md is None and i < 5:
            gevent.sleep(1)
            i += 1
        else:
            if md is None:
                print'get code price fail' % code
                return price

        if pl > 100:
            r = float(pl) / 100000
            if base_pb2.OPR_BUY == bs_flag:
                price = md.match * (1 + r)
                if price > md.high_limited:
                    price = md.high_limited
            elif base_pb2.OPR_SELL == bs_flag:
                price = md.match * (1 - r)
                if price < md.low_limited:
                    price = md.low_limited
            else:
                print'error bs flag 0x%x' % (bs_flag)
                price = md.ask_price
            return price
        elif base_pb2.LIMIT_DOWN == pl:
            price = md.low_limited
        elif base_pb2.LIMIT_UP == pl:
            price = md.high_limited
        elif base_pb2.PRICE_MATCH == pl:
            price = md.match
        elif pl > base_pb2.PRICE_MATCH:
            price = md.bid_price[pl - base_pb2.S_1]
        elif pl >= base_pb2.B_10:
            price = md.ask_price[pl - base_pb2.B_10]
        else:
            price = md.match
            print'error price level %d' % (pl)
        return price
    @classmethod
    def get_price_by_price_level(cls, code, pl, bs_flag):
        price = 0
        i = 0
        md = cls.get_real_time_md(code)
        while md is None and i < 5:
            gevent.sleep(1)
            i += 1
        else:
            if md is None:
                print'get code price fail: [%s]' % code
                return price

        if pl > 100:
            r = float(pl) / 100000
            if base_pb2.OPR_BUY == bs_flag:
                price = md.match * (1 + r)
                if price > md.high_limited:
                    price = md.high_limited
            elif base_pb2.OPR_SELL == bs_flag:
                price = md.match * (1 - r)
                if price < md.low_limited:
                    price = md.low_limited
            else:
                print'error bs flag 0x%x' % (bs_flag)
                price = md.ask_price
            return price
        elif base_pb2.LIMIT_DOWN == pl:
            price = md.low_limited
        elif base_pb2.LIMIT_UP == pl:
            price = md.high_limited
        elif base_pb2.PRICE_MATCH == pl:
            price = md.match
        elif pl > base_pb2.PRICE_MATCH:
            price = md.ask_price[pl - base_pb2.S_1]
        elif pl >= base_pb2.B_10:
            price = md.bid_price[base_pb2.B_1-pl]
        else:
            price = md.match
            print'error price level %d' % (pl)
        return price


if __name__ == "__main__":
    pass
