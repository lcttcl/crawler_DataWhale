# -*- coding: utf-8 -*-
"""
@File    :   t1.py
@Author  :   Li Changtai
@E-mail  :   lichangtai17@gmail.com
@Date    :   2019/8/6 12:35
@Software:   PyCharm
"""

import requests
import re
import csv
import pandas as pd


info = {
        'rank': [],
        'name': [],
        'country': [],
        'director': [],
        'score': []
    }
rs = pd.DataFrame(info)


def get_info(url):
    global rs
    res = requests.get(url)
    ranks = re.findall(' <em class="">(.*?)</em>', res.text, re.S)
    names = re.findall('<span class="title">([\u4e00-\u9fa5]+)</span>', res.text, re.S)
    countries = re.findall('&nbsp;/&nbsp;([\u4e00-\u9fa5]+)&nbsp;/&nbsp;', res.text, re.S)
    text = re.sub('导演: ', "", res.text)
    directors = re.findall('<p class="">(.*?)&nbsp;&nbsp;', text, re.S)
    scores = re.findall('<span class="rating_num" property="v:average">(.*?)</span>', res.text, re.S)

    for rank, name, country, director, score in zip(ranks, names, countries, directors, scores):
        new_line = pd.Series([rank, name, country, director, score],
                             index=list(['rank', 'name', 'country', 'director', 'score']))
        new_line = pd.DataFrame(new_line).T
        rs = pd.concat([rs, new_line], axis=0)


if __name__ == '__main__':
    for i in range(0, 250, 25):
        url = 'https://movie.douban.com/top250?start={}&filter='.format(i)
        get_info(url)

    rs.index = list(range(1, len(rs)+1))
    rs.to_csv('movie_rank_info.csv')