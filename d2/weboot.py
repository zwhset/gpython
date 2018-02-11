# -*- coding: utf-8 -*-
"""
    package.module
    ~~~~~~~~~~~~~~

    一个微信机器人程序

    微信客户端itchat:
        http://itchat.readthedocs.io/
    机器人聚合API：
        ## params
        - info 发给机器人的信息
        - dtype json|xml
        - loc 地点
        - userid 1-32位，可以用于上下文关联

        http://op.juhe.cn/robot/index?info=%E5%8C%97%E4%BA%AC&dtype=&loc=&userid=1&key=978f281744b2cda30642dbbaf3eb8349

"""

import itchat
import requests

def xiao_ai(say):
    '''调用聚合机器人接口实现自动回复，逻辑层次可以在这里面加'''
    url = 'http://op.juhe.cn/robot/index'
    params = {
        'info' : say,
        'userid' : 1,
        'key' : '978f281744b2cda30642dbbaf3eb8349'
    }
    r = requests.get(url, params)
    data = r.json()

    if data['error_code'] != 0:
        return 'xiaoai病了，过会再问吧'

    result = data['result']
    text = result['text']
    url = result.get('url', '')

    recv = text + url
    return recv

@itchat.msg_register(itchat.content.TEXT)
def recv_content(msg):
    say = msg['Text']
    itchat.send(xiao_ai(say)) # 呼叫小爱同学

if __name__ == '__main__':
    itchat.auto_login(enableCmdQR=2) # hotReload=True
    itchat.run()