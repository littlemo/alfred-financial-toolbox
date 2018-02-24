#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import argparse

import workflow


def init_args_parser():
    des = u'''用例：
    ./earning.py 6000 30 5  # 6000元购买30天期，年化收益率5%的固收理财'''
    parser = argparse.ArgumentParser(
        prog='earning',
        description=des,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        'capital', type=float,
        help=u'待理财本金，单位元')
    parser.add_argument(
        'days', type=int,
        help=u'理财周期，单位天')
    parser.add_argument(
        'returns', type=float,
        help=u'年化收益率，单位%')
    return parser


def calc_profits(data):
    profits = data.capital * data.returns * data.days / 36500
    return profits


def get_subtitle_tucao(p):
    '''获取入参回显的子标题吐槽信息'''
    subtitle = u''
    if p.capital >= 100000:
        subtitle = u'大佬，您还缺pong友么？借钱不还的那种~~'
    if p.returns >= 10:
        subtitle = u'大佬，这么高收益，您是怎么理财的？教教小的我吧(笑cry)~~'
    return subtitle


def main(wf):
    argv_len = len(sys.argv)
    if argv_len < 4 or argv_len > 5:
        wf.add_item(
            u'[计算] {}'.format(
                ' '.join(sys.argv[1:])),
            subtitle=u'本金、天数、年化收益率(%)')
        wf.send_feedback()

    parser = init_args_parser()
    p = parser.parse_args()
    subtitle = get_subtitle_tucao(p)

    title = u'{capital}元购买{days}天期，年化收益率{returns}%的固收理财'.format(
        capital=p.capital,
        days=p.days,
        returns=p.returns)
    wf.add_item(
        title,
        subtitle=subtitle,
        valid=False,
        arg=title,
        largetext=title)
    profits = calc_profits(p)
    result_title = u'[结果]收益：{:>6,.2f}'.format(profits)
    wf.add_item(
        result_title,
        subtitle=u'本金：{:>6,.2f}，天数：{:>6,.2f}'.format(
            p.profits, p.days),
        valid=False,
        icon=workflow.ICON_NOTE,
        arg=result_title,
        copytext=result_title)
    wf.send_feedback()


if __name__ == u'__main__':
    wf = workflow.Workflow()
    sys.exit(wf.run(main))
