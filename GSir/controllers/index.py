# -*- coding: utf-8 -*-
"""
    package.module
    ~~~~~~~~~~~~~~

    控制层首页模块

    :copyright: (c) YEAR by zwhset.
    :license: GOMEOPS, see LICENSE_FILE for more details.
"""

import sys

from flask import Blueprint, render_template
from modules import users

if sys.version_info[0] < 3:
    reload(sys)
    sys.setdefaultencoding('utf8')

b_index = Blueprint('b_index', __name__)

@b_index.route('/')
@b_index.route('/index')
@users.is_login
def index():
    '''首页'''
    return render_template('base.html')