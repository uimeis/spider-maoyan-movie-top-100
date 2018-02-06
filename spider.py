# -*- coding:utf-8 -*-
#Author: uimeis

import requests
from bs4 import BeautifulSoup
import pandas

#取出单个数据
def Onepage(num, y):
    url = 'http://maoyan.com/board/4?offset={}'.format(y*10)
    result = {}
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'}
    res = requests.get(url, headers=header)
    soup = BeautifulSoup(res.text, 'html.parser')
    result['title'] = soup.select('.image-link')[num]['title'] #取出标题
    result['actor'] = soup.select('.star')[num].text.lstrip('\n        ').rstrip('\n                ').split('：')[-1] #取出演员
    result['time'] = soup.select('.releasetime')[num].text.split('：')[-1] #取出时间
    result['score'] = soup.select('.score')[num].text #取出评分
    result['img_url'] = soup.select('.board-img')[num]['data-src'].split('@')[0] #取出封面图片
    return result

#取出一页10个电影数据
def Onepagelist(y):
    onepage = []
    for i in range(10):
        onepage.append(Onepage(i,y))
    return onepage

#取出10页100个电影数据
total = []
for y in range(10):
    total.extend(Onepagelist(y))
print(len(total))

#保存excel格式
df = pandas.DataFrame(total)
df.to_excel('maoyan.xlsx')
