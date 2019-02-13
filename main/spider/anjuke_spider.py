#-*-coding:utf-8-*-
'''爬虫类'''
import time
import requests
from bs4 import BeautifulSoup
from main.model.anjuke import anjuke_house
from main.util.dbutil import *

# 获取指定url的网页源码
def get_html(url):
    # 设置请求头，防止被网站屏蔽
    headers  = {
        'User-Agent':'User-Agent:Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    }
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        print(url)
        return resp.text
    return None

# 获取一页数据
def get_data(url):
    # 获取网页源码
    html = get_html(url)

    soup = BeautifulSoup(html, 'lxml')
    # 获取房屋详情
    details = soup.select('div.zu-info > h3 > a')
    # 获取户型
    types = soup.select('p.tag')
    # 获取房屋价格
    prices = soup.select('strong')
    # 获取小区名称
    villages = soup.select('div.zu-info > address > a')

    # 创建表格
    create_table()

    # 保存数据
    for detail,house_type,price,village in zip(details,types,prices,villages):
        # 获取房屋描述
        detail = detail.get_text()
        # 获取户型
        house_type = house_type.get_text().strip().split('|')[0]
        # 获取房屋价格
        price = price.get_text()
        # 获取小区名称
        village = village.get_text()
        # 实例化对象并绑定数据
        house = anjuke_house(detail=detail, house_type=house_type, price=price, village=village)
        # 将数据保存到数据库
        save(house)

    # 获取下一页地址
    next_page = soup.select('a.aNxt')
    if len(next_page) > 0:
        return next_page[0]['href']
    return None

# 分页爬取
if __name__ == '__main__':
    # 记录起始时间
    start_time = time.time()
    # 设定起始页
    url = 'https://cd.zu.anjuke.com/?from=navigation'
    while True:
        time.sleep(1.5) # 减慢访问频率，防止出现验证
        url = get_data(url)
        if None==url:
            break
    # 计算总共花费的时间
    print('totally took %s seconds.' % int(time.time()-start_time))