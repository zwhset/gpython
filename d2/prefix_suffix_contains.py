# -*- coding: utf-8 -*-
"""
    package.module
    ~~~~~~~~~~~~~~

    字符串的一些方法
    and -> 左 and 右 左右都为真则返回真

    :copyright: (c) YEAR by zwhset.
    :license: GOMEOPS, see LICENSE_FILE for more details.
"""


def has_prefix(s, prefix):
    '''前缀判断

    len(s) >= len(prefix) 如果s的长度要比prefix少肯定是错误的 s = 'ab' prefix='abcdsd' 肯定是错误的
    s[:len(prefix)] # 即分片取prefix的长度就成为一个字符串判断相等即可
    '''
    return len(s) >= len(prefix) and s[:len(prefix)] == prefix

def has_suffix(s, suffix):
    '''后缀判断

    同理取反
    '''
    return len(s) >= len(suffix) and s[len(s)-len(suffix):] == suffix

def contains(s, substr):
    '''包含判断

    循环取索引，依次尝试用索引位置去尝试前缀判断即可。满足前缀即满足包含。
    '''
    for i, _ in enumerate(s):
        if has_prefix(s[i:], substr):
            return True

    return False
