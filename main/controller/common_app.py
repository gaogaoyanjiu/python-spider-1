# -*-coding:utf-8-*-
"""普通请求类"""
from flask import Blueprint, render_template
from main.service.anjuke_service import *

# 创建蓝图对象
common = Blueprint('common', __name__)


# 返回总数据条数
@common.route('/')
def index():
    return '共有数据%s条' % get_all_count()


# 统计户型分布情况
@common.route('/type')
def type_distribution():
    data = get_house_type()
    # 将数据绑定到页面上
    return render_template("type.html", nums=list(data.values()), types=list(data.keys()))


# 统计某户型的租金分布情况，<XXX>代表参数
@common.route('/type/<house_type>')
def rent_distribution(house_type):
    data = get_rent_by_house_type(eval(house_type))
    return render_template("rent.html", prices=list(data.keys()), nums=list(data.values()))


# 生成房屋描述词云图
@common.route('/wordcloud')
def wordcloud():
    words = get_details()
    return render_template("wordcloud.html", words=list(words.keys()), nums=list(words.values()))


# 跳转汇总分析页面
@common.route('/overall')
def overall():
    return render_template("overall.html")
