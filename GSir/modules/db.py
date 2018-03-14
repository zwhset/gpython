# -*- coding: utf-8 -*-
"""
    package.module
    ~~~~~~~~~~~~~~

    数据库模块
        mysql object

    :copyright: (c) YEAR by zwhset.
    :license: GOMEOPS, see LICENSE_FILE for more details.
"""
import sys

if sys.version_info[0] < 3:
    reload(sys)
    sys.setdefaultencoding('utf8')

import pymysql

from .config import CONFIG


class Mysql(object):
    '''mysql 数据库'''

    def __init__(self, dict=True):
        '''

        :param dict: 为正为回字典，为假返回元组
        '''
        self.dict = dict
        self._config_parse()

    def _execute(self, query):
        '''公用执行方法'''
        try:
            self.cursor.execute(query)
        except:
            self._config_parse()
            self.cursor.execute(query)

    def fetchone(self, query):
        '''获取数据库的一条记录'''
        self._execute(query)
        return self.cursor.fetchone()

    def fetchall(self, query):
        '''获取所有数据'''
        self._execute(query)
        return self.cursor.fetchall()

    def write(self, query):
        '''数据库的写方法'''
        self._config_parse() # 避免连接问题，先初始化链接没错的
        count = self.cursor.execute(query)
        self.conn.commit()

        return count

    def _config_parse(self):
        '''解析配置文件获得连接对象'''
        section = 'MYSQL'
        parmas = {
            'host': CONFIG.get(section, 'host'),
            'port': int(CONFIG.get(section, 'port')),
            'user': CONFIG.get(section, 'user'),
            'password': CONFIG.get(section, 'password'),
            'db': CONFIG.get(section, 'database'),
            'charset': CONFIG.get(section, 'charset')
        }

        if self.dict: # 获取字典方式返回数据
            parmas["cursorclass"] = pymysql.cursors.DictCursor

        self.conn = pymysql.connect(**parmas)
        self.cursor = self.conn.cursor()
