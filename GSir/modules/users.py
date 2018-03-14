# -*- coding: utf-8 -*-
"""
    package.module
    ~~~~~~~~~~~~~~

    用户模块
        注册方法
        登陆检查

    :copyright: (c) YEAR by zwhset.
    :license: GOMEOPS, see LICENSE_FILE for more details.
"""
import sys

if sys.version_info[0] < 3:
    reload(sys)
    sys.setdefaultencoding('utf8')

from hashlib import md5
from flask import session, redirect
from functools import wraps

from .db import Mysql

def is_login(func):
    '''是否登陆的装饰器'''
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not session.get('username', None):
            return redirect('/login')
        return func(*args, **kwargs)
    return wrapper

class Users(Mysql):
    '''用户类方法'''
    def __init__(self):
        super(Users, self).__init__()
        self._table_name = 'users'

    def login(self, phone, password):
        '''登陆方法，此处为登陆的入口'''
        try:
            phone = int(phone)
        except:
            return False, '手机号格式不对'

        return self._check_login(phone, password)

    def register(self, phone, username, password, sex=0, wechat='', status=1):
        '''注册方法'''

        # 参数检查
        if not phone or not username or not password:
            return False, '手机号、用户名、密码不能为空'

        if len(password) < 5:
            return False, '密码长度太过于简单'

        if len(username) < 2:
            return False, '用户名长度过短'

        if sex not in (0, 1, '0', '1'):
            sex = 0 # 默认为女
        sex = int(sex)

        if status not in (0, 1, '0', '1'):
            status = 0 # 默认不激活
        status = int(status)

        if not self._check_phone(phone):
            return False, '手机号已经存在，请更新手机号。'

        password = self.encry_password(password)

        # 入库， 到这里如果不是数据库问题则必然可以注册成功
        try:
            if self._reg_db(phone, username, password, sex, wechat, status):
                return True, '注册成功'
            return False, '注册失败，数据库故障'
        except Exception as e:
            return False, '注册失败，错误信息： {0}'.format(str(e))

    def _reg_db(self, phone, username, password, sex=None, wechat=None, status=1):
        '''实际注册方法'''
        query = '''
            INSERT INTO
              {table_name}(phone, username, password, sex, wechat, status)
            VALUES({phone}, "{username}", "{password}", {sex}, "{wechat}", {status})
        '''.format(table_name=self._table_name,
                   phone=phone,
                   username=username,
                   password=password,
                   sex=sex,
                   wechat=wechat,
                   status=status)
        if self.write(query):
            return True
        return False

    def _check_phone(self, phone):
        '''验证手机号是否在数据库中已经存在，存在不能注册'''
        query = '''
            SELECT
              phone
            FROM
              {table_name}
            WHERE
              phone={phone}              
        '''.format(table_name=self._table_name, phone=phone)
        if self.fetchone(query): # 如果存在返回不能注册
            return False
        return True

    def _check_login(self, phone, password):
        '''测试登陆是否正常'''

        if not phone or not password:
            return False, '手机号与密码不能为空'

        query = '''
            SELECT 
              phone, password, status, username
            FROM
              {table_name}
            WHERE
              phone={phone}
        '''.format(table_name=self._table_name, phone=phone)

        data = self.fetchone(query)
        if not data:
            return False, '用户不存在'

        if not data['status']:
            return False, '用户未激活'

        password = self.encry_password(password)
        if not (data['password'] == password):
            return False, '密码不正确'

        return True, (data['username'], data['phone'])

    def encry_password(self, password):
        return md5(password.encode('utf-8')).hexdigest()
