# -*- coding: utf-8 -*-
"""
    package.web
    ~~~~~~~~~~~~~~

    Gsir 启动入口

    :copyright: (c) YEAR by zwhset.
    :license: GOMEOPS, see LICENSE_FILE for more details.
"""

from flask import Flask

app = Flask(__name__)
# Secret Key
app.config['SECRET_KEY'] = 'slkfjlweihow32j1ljnslafsfji32'


# 导入url 控制层
from controllers.users import b_users
from controllers.index import b_index

# 注册蓝图
app.register_blueprint(b_users)
app.register_blueprint(b_index)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, threaded=True, debug=True)