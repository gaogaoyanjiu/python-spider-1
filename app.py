# -*-coding:utf-8-*-
"""服务器网关接口类"""
from flask import Flask
from main.controller.common_app import common
from main.controller.ajax_app import ajax

# 实例化WSGI应用对象
app = Flask(__name__)

# 注册普通请求蓝图对象
app.register_blueprint(common, url_prefix='')
# 注册异步请求蓝图对象
app.register_blueprint(ajax, url_prefix='/ajax')

if __name__ == '__main__':
    # 设置debug=True，更改了代码之后会自动重新加载，不用手动重新运行
    app.run(debug=True)