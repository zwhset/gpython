# -*- coding: utf-8 -*-
"""
    package.module
    ~~~~~~~~~~~~~~

    A brief description goes here.

    :copyright: (c) YEAR by AUTHOR.
    :license: LICENSE_NAME, see LICENSE_FILE for more details.
"""

# 输入 输出
def login(username, password, code):
    '''login fucntion'''
    # check username password
    if not(username == 'zwhset' and password == '123456'):
        return "用户和密码不正确"
    # check code
    if code != '8888':
        return '验证码失败'
    return '登陆成功'

    # if username == 'zwhset' and password == '123456' :
    #     if code == '8888':
    #         print "登陆成功"
    #     else:
    #         print "验证码失败"
    # else:
    #     print "用户和密码不正确"

print login(username='asfa', password='123456', code='8888')
