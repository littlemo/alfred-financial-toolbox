#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import argparse


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
