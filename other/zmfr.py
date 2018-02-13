# -*- coding: utf-8 -*-
from __future__ import print_function
"""
    package.module
    ~~~~~~~~~~~~~~

    gmap: 一段实现兼容性的内置map函数
"""
import sys
PY_VERSION = sys.version_info[0]

def gmap(func, *args):
    """
    map(function, sequence[, sequence, ...]) -> list

    Return a list of the results of applying the function to the items of
        the argument sequence(s).  If more than one sequence is given, the
        function is called with an argument list consisting of the corresponding
        item of each sequence, substituting None for missing values when not all
        sequences have the same length.  If the function is None, return a list of
        the items of the sequence (or a list of tuples if more than one sequence).
    """

    if not isinstance(args, (list, tuple)):
        raise(ValueError, 'args need iter')

    args = zip(*args) # ((1,2), (3,4)) -> ((1,3), (2,4))

    # 两种实现方式

    # 1. 生成器表达式实现
    ret = ( func(*p) for p in args )

    # 2. 生成器函数实现
    # def go_ret(args):
    #     for p in args:
    #         yield func(*p)
    # ret = go_ret(args)

    if PY_VERSION < 3:
        return list(ret)

    return ret

def gfilter(func, *args):
    """
    gfilter(function, sequence[, sequence, ...]) -> list

    """

    if not isinstance(args, (list, tuple)):
        raise(ValueError, 'args need iter')

    args = zip(*args) # ((1,2), (3,4)) -> ((1,3), (2,4))

    # 两种实现方式

    # 1. 生成器表达式实现
    ret = ( func(*p) for p in args if p )

    # 2. 生成器函数实现
    def go_ret(args):
        for p in args:
            y = func(*p)
            if y:
                yield y
    ret = go_ret(args)

    if PY_VERSION < 3:
        return list(ret)

    return ret

def greduce():
    pass

def gzip():
    pass
