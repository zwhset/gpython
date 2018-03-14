# -*- coding: utf-8 -*-
"""
    package.module
    ~~~~~~~~~~~~~~

    控制层用户模块

    :copyright: (c) YEAR by zwhset.
    :license: GOMEOPS, see LICENSE_FILE for more details.
"""

import sys

if sys.version_info[0] < 3:
    reload(sys)
    sys.setdefaultencoding('utf8')

from flask import (Blueprint, render_template, jsonify,
                   flash, request, redirect, url_for,
                   session)
b_users = Blueprint('b_users', __name__)

from modules import users

user = users.Users()

@b_users.route('/login', methods=['POST', 'GET'])
def login():
    '''登陆路由'''
    if request.method == 'POST':
        phone = request.form.get('phone', None)
        password = request.form.get('password', None)
        ok, message = user.login(phone, password)
        if not ok:
            flash(message, 'danger')
            return render_template('login.html')
        username, _ = message
        session['username'] = username

        return redirect('/index')

    return render_template('login.html')

@b_users.route('/logout')
def logout():
    '''登出'''
    del session['username']
    return redirect('/index')

@b_users.route('/register', methods=['POST', 'GET'])
def register():
    '''注册路由'''

    if request.method == 'POST':
        phone = request.form.get('phone', None)
        username = request.form.get('username', None)
        password = request.form.get('password', None)
        password2 = request.form.get('password2', None)
        wechat = request.form.get('wechat', None)
        sex = request.form.get('sex', None)

        if password != password2:
            flash('两次密码不一致', 'danger')
            return render_template('register.html',
                                   phone=phone,
                                   username=username,
                                   wechat=wechat,
                                   sex=sex)

        ok, message = user.register(phone, username, password, sex, wechat)
        if not ok:
            flash(message, 'danger')
            return render_template('register.html',
                                   phone=phone,
                                   username=username,
                                   wechat=wechat,
                                   sex=sex)

        session['username'] = username
        return redirect('/index')

    return render_template('register.html')