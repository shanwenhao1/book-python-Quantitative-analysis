#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/13
# @Author  : wenHao shan
# @Dsc     : the example of quantification

import numpy as np


def sta001(k: float, nyear: int, xd: float):
    """
    量化复利收益函数
    :param k:
    :param nyear:
    :param xd:
    :return:
    """
    d2 = np.fv(k, nyear, -xd, -xd)
    d2 = round(d2)
    return d2


def sta001_example_1():
    """
    量化复利收益示例函数1
    :return:
    """
    d40 = 1.4 * 40
    print("d40, 40 * 1.4=", d40)
    d = sta001(0.05, 40 - 1, 1.4)
    print("01保守投资模式, 每年定期存入1.4万元, 年收益5%", "40年后资产: %f, 投资回报率: %f"%(d, round(d / d40)))

    d2 = sta001(0.20, 40 - 1, 1.4)
    print("02激进投资模式, 每年定期存入1.4万元, 年收益20%", "40年后资产: %f, 投资回报率: %f"%(d2, round(d2 / d40)))

    dk = round(d2 / d)
    print("dk, 两者收益差别(xx倍): ", dk)


if __name__ == '__main__':
    sta001_example_1()
