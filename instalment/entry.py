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
        profits *= (1 + data.returns / 100 / 12)
        # 分期手续费
        fee += fee_per_stages
        # 填充列表
        rc.append([x + 1, profits_his, profits, fee_per_stages])
        # 偿还本金
        profits -= data.cost / data.stages
    rc.append([None, profits, profits, None])
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

    title = u'将{cost}元分{stages}期，年化收益率{returns}%，月分期费率{fee}%'.format(
        cost=p.cost,
        stages=p.stages,
        returns=p.returns,
        fee=p.fee)
    wf.add_item(
        title,
        valid=False,
        arg=title,
        largetext=title)
    profits, fee, rc = calc_retained_profits(p)
    largetext = u''
    for item in rc[:-1]:
        largetext += u'{stage:02d}期\t月初：￥{balance_his:>10,.2f}\t' \
            u'月末：￥{balance:>10,.2f}\t费用：￥{fee:>10,.2f}\n'.format(
                stage=item[0],
                balance_his=item[1],
                balance=item[2],
                fee=item[3]
            )
    cost_per_month = p.cost / p.stages
    fee_per_month = p.cost * p.fee / 100
    largetext += u'[月缴本金]：{:>10,.2f}\n'.format(cost_per_month)
    largetext += u'[月缴费用]：{:>10,.2f}\n'.format(fee_per_month)
    largetext += u'[最终收益]：{:>10,.2f}'.format(rc[-1][1])
    wf.add_item(
        u'[结果]收益：{:>6,.2f}，费用：{:>6,.2f}，净收益：{:>6,.2f}'.format(
            profits, fee, profits - fee),
        subtitle=u'月缴本金：{:>6,.2f}，月缴费用：{:>6,.2f}'.format(
            cost_per_month, fee_per_month),
        valid=True,
        icon=workflow.ICON_NOTE,
        arg=largetext,
        largetext=largetext,
        copytext=largetext)
    wf.send_feedback()


if __name__ == u'__main__':
    wf = workflow.Workflow()
    sys.exit(wf.run(main))
