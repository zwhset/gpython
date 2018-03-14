# -*- coding: utf-8 -*-
from __future__ import print_function
"""
    package.module
    ~~~~~~~~~~~~~~

    处理配置文件方法

    usage:
        from modules.config import CONFIG

        hostname = CONFIG.get('mysql', 'host')

    :copyright: (c) YEAR by zwhset.
    :license: GOMEOPS, see LICENSE_FILE for more details.
"""

import os
import sys

if sys.version_info[0] < 3:
    reload(sys)
    sys.setdefaultencoding('utf8')

try:
    from ConfigParser import ConfigParser
except:
    from configparser import ConfigParser


config_path = 'conf.ini'

if not os.path.isfile(config_path):
    print('conf.ini not fund.')
    sys.exit(1)

CONFIG = ConfigParser()
CONFIG.read(config_path)