# -*-coding:utf-8-*-
"""异步请求类"""
import math
from flask import Blueprint, request
from flask.json import jsonify
from main.service.anjuke_service import *

# 创建蓝图对象
ajax = Blueprint('ajax', __name__)


# 获取某类型房屋租金分布情况数据
@ajax.route('/getRentByType', methods=['POST'])
def get_rent_by_type():
    temp = get_rent_by_house_type(request.form.get('type'))
    data = {'prices': list(temp.keys()), 'pnums': list(temp.values())}
    return jsonify(data)


# 获取房屋类型分布情况数据
@ajax.route('/getTypeAJAX', methods=['POST'])
def get_type_ajax():
    temp = get_house_type()
    types = list(temp.keys())
    data = []
    for house_type in types:
        data.append({'value': temp[house_type], 'name': house_type})
    return jsonify({'types': types, 'data': data})


# 获取词云数据
@ajax.route('/getWordsAJAX', methods=['POST'])
def get_words_ajax():
    words = get_details()
    data = []
    for word in words.keys():
        data.append({'name': word, 'value': math.sqrt(words[word])})
    return jsonify({'data': data})
