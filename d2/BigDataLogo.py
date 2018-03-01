# -*- coding: utf-8 -*-
from __future__ import print_function

"""
    package.module
    ~~~~~~~~~~~~~~

    处理大数据文件
    
    :copyright: (c) YEAR by zwhset.
    :license: GOMEOPS, see LICENSE_FILE for more details.
"""

import time
from datetime import datetime

def run(function):
    '''
    ➜  d2 git:(master) ✗ time python2.7 BigDataLogo.py
    start:  1519884820.18
    runtime:  96.0794770718 S
    python2.7 BigDataLogo.py  81.33s user 7.84s system 92% cpu 1:36.24 total

    ➜  d2 git:(master) ✗ time python3.6 BigDataLogo.py
    start:  1519884935.979166
    runtime:  102.83143186569214 S
    python3.6 BigDataLogo.py  86.65s user 10.66s system 94% cpu 1:43.19 total
    '''

    st = time.time()
    print('start: ', st)
    function()
    et = time.time()
    print('runtime: ', et-st, 'S')

def an():
    with open('ops.gmfcloud.com_access.log') as fd:
        for line in fd:
            log = line.split('||')

#run(an)

import pymysql

parmas = {
            'host' : 'localhost',
            'port' : 3306,
            'user' : 'root',
            'password' : '',
            'db' : 'nginx_log',
            'charset' : 'utf8',
        }
conn = pymysql.connect(**parmas)
cursor = conn.cursor()

def parsetime(string):
    # '17/Mar/2017:16:13:27'
    return datetime.strptime(string, "%d/%b/%Y:%H:%M:%S")

def insert(log, i):
    n = len(log)
    cn = '"%s", ' * n
    cn = cn[:-2]

    query = '''
        INSERT INTO log(
            status,time_local,remote_addr,http_x_forwarded_for,request,query_string,
            body_bytes_sent,http_referer,request_time,http_user_agent,http_cookie,
            host,upstream_addr,upstream_response_time,upstream_status,server_addr
        )
        VALUES(
            %s
        )
    ''' % cn
    query = query % tuple(log)
    try:
        cursor.execute(query)
    except Exception as e:
        print(i)
        print(query)

        raise e


def read_log(filename='ops.gmfcloud.com_access.log'):
    with open(filename) as fd:
        i = 0
        for line in fd:
            i += 1
            # cc
            line = line.replace('[', '')
            line = line.replace(']', '')
            line = line.replace('up_addr:', '')
            line = line.replace('up_resp:', '')
            line = line.replace('up_status:', '')

            log = [ l.strip() for l in  line.split('||')]
            log[1] = parsetime(log[1].split(' ')[0])

            if not isinstance(log[-3], int):
                log[-3] = 0
            if not isinstance(log[-2], int):
                log[-2] = 0

            insert(log, i)

            if ( i % 1000.0) == 0:
                print(i)
                conn.commit()

        conn.commit()

read_log()
