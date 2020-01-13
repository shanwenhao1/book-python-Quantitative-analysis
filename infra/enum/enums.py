#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/13
# @Author  : wenHao Shan


class Enum(object):
    """
    枚举基类
    """
    def __init__(self, **kwargs):
        self.dict = kwargs
        for key, value in kwargs.items():
            setattr(self, key, value)

        self.key_list = kwargs.keys()
        self.value_list = kwargs.values()
