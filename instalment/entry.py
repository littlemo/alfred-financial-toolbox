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


def main(wf):
    argv_len = len(sys.argv)
    if argv_len < 4 or argv_len > 5:
        wf.add_item(
            u'(金额/分期/收益率/月费率)：{}'.format(
                ' '.join(sys.argv[1:])))
        wf.send_feedback()

    parser = init_args_parser()
    p = parser.parse_args()

    wf.add_item(
        u'将{cost}元分{stages}期，年化收益率{returns}%，月分期费率{fee}%'.format(
            cost=p.cost,
            stages=p.stages,
            returns=p.returns,
            fee=p.fee))
    profits, fee, rc = calc_retained_profits(p)
    largetext = u'期数\t月初金额\t月末金额\t当月手续费'
    for item in rc:
        item_format = item
        item_format[1] = round(item[1], 2)
        item_format[2] = round(item[2], 2)
        item_format[3] = round(item[3], 2) if item[3] else None
        largetext += u'\n' + '\t'.join(item_format)
    wf.add_item(
        u'[结果]收益：{}，费用：{}，净收益：{}'.format(
            profits, fee, profits - fee),
        subtitle=u'可键入 ⌘L 查看放大的详细列表信息',
        valid=True,
        largetext=largetext,
        copyright=largetext)
    wf.send_feedback()
