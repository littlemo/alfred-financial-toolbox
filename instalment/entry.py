#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import argparse

import workflow


def init_args_parser():
    des = u'''用例：
    ./entry.py 6000 12 4  # 将6000元分12期，年化收益率4%，月分期费率0%'''
    parser = argparse.ArgumentParser(
        prog='instalment',
        description=des,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        'cost', type=float,
        help=u'待分期金额，单位元')
    parser.add_argument(
        'stages', type=int,
        help=u'分期数')
    parser.add_argument(
        'returns', type=float,
        help=u'年化收益率，单位%')
    parser.add_argument(
        'fee', type=float, default=0, nargs='?',
        help=u'月分期费率，单位%，默认为0')
    return parser


def calc_retained_profits(data):
    rc = []
    fee = 0
    profits = data.cost
    fee_per_stages = data.cost * data.fee / 100
    for x in xrange(0, data.stages):
        # 月初余额
        profits_his = profits
        # 月末余额
        profits *= (1 + data.returns / 100) / 12
        # 分期手续费
        fee += fee_per_stages
        # 填充列表
        rc.append([x + 1, profits_his, profits, fee_per_stages])
        # 偿还本金
        profits -= data.cost / data.stages
    rc.append([None, profits, profits, None])
    print(u'收益：{}，费用：{}，净收益：{}'.format(
        profits, fee, profits - fee))

    return profits, fee, rc
