#-*-coding:utf-8-*-
'''服务器网关接口类'''
from flask import Flask, render_template
from main.util.dbutil import *
from main.util.wordutil import *

# 实例化WSGI应用对象
app = Flask(__name__)

# 返回总数据条数
@app.route('/')
def index():
    # 执行SQL语句，查询总数据条数
    results = execute_sql('SELECT COUNT(id) FROM anjuke')
    # 从元组中拿到结果
    total = tuple(results)[0][0]
    return '共有数据%s条' % total

# 统计户型分布情况
@app.route('/type')
def type_distribution():
    results = execute_sql('SELECT COUNT(id) num,house_type FROM anjuke GROUP BY house_type')
    nums = []
    types = []
    for result in results:
        nums.append(result.num)     # 对应户型房屋数量
        types.append(result.house_type)     # 房屋户型
    # 将数据绑定到页面上
    return render_template("type.html",  nums = nums, types = types)

# 统计某户型的租金分布情况，<XXX>代表参数
@app.route('/type/<house_type>')
def rent_distribution(house_type):
    results = execute_sql("SELECT price,COUNT(id) num FROM anjuke WHERE house_type=%s GROUP BY price" % house_type)
    prices = []
    nums = []
    for result in results:
        prices.append(result.price)     # 租金
        nums.append(result.num)     # 对应租金的房屋数量
    return render_template("rent.html", prices = prices, nums = nums)

# 生成房屋描述词云图
@app.route('/wordcloud')
def wordcloud():
    words = get_details()
    return render_template("detail.html", words = list(words.keys()), nums = list(words.values()))

if __name__ == '__main__':
    # 设置debug=True，更改了代码之后会自动重新加载，不用手动重新运行
    app.run(debug=True)