# -*-coding:utf-8-*-
"""Service类"""
from main.util.dbutil import execute_sql
from main.util.wordutil import cut_word


# 获取总记录条数
def get_all_count():
    # 执行SQL语句，查询总数据条数
    results = execute_sql('SELECT COUNT(id) FROM anjuke')
    # 返回总记录条数
    return tuple(results)[0][0]


# 获取房屋类型数据
def get_house_type():
    results = execute_sql('SELECT COUNT(id) num,house_type FROM anjuke GROUP BY house_type')
    data = {}
    for result in results:
        data[result.house_type] = result.num
    return data


# 根据户型获取租金分布情况
def get_rent_by_house_type(house_type):
    results = execute_sql(
        "SELECT price,COUNT(id) num FROM anjuke WHERE house_type='%s' GROUP BY price ORDER BY price ASC" % house_type)
    data = {}
    for result in results:
        data[result.price] = result.num
    return data


# 获取房屋描述词语频次详情
def get_details():
    results = execute_sql('SELECT detail FROM anjuke')
    words = []
    for detail in tuple(results):
        words.extend(cut_word(detail[0]))
    result = {}
    for word in words:
        if ' ' in word:
            pass  # 舍弃空白结果
        elif word in result:
            result[word] += 1  # 若词语已存在，则其值加一
        else:
            result.update({word: 1})  # 若词语不存在，则新增到结果里
    return result
