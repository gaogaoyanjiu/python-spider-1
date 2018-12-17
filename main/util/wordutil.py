#-*-coding:utf-8-*-
'''词云分析工具类'''
import jieba
from main.util.dbutil import *

# 获取房屋描述词语频次详情
def get_details():
    results = execute_sql('SELECT detail FROM anjuke')
    words = []
    for detail in tuple(results):
        words.extend(list(jieba.cut(detail[0])))    # 使用jieba分词，将分词结果存入列表
    result = {}
    for word in words:
        if ' ' in word:
            pass    # 舍弃空白结果
        elif word in result:
            result[word] += 1   # 若词语已存在，则其值加一
        else:
            result.update({word:1})   # 若词语不存在，则新增到结果里
    return result