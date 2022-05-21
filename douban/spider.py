'''
2022年1月19日
'''
import os
import re
import sys
import urllib.error as error
from urllib import request

import xlwt
from bs4 import BeautifulSoup as bf

from init_config import PraseConfig
from sqlHelper import SqlHelper

CONF = PraseConfig()

MOIVE_LINK = re.compile(r'<a href="(.*?)">')
IMG_LINK = re.compile(r'<img.*src="(.*?)"', re.S)  # 忽略换行符
NAME = re.compile(r'<span class="title">(.*)</span>')
RATE = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
JUDGE_NUM = re.compile(r'<span>(\d*)人评价</span>')
INQ = re.compile(r'<span class="inq">(.*)</span>')


def get_data(base_url):
    '''
    爬取网页数据
    '''
    print("获取数据中....")
    data_list = []
    rank = 0
    for i in range(0, 10):
        html = ask_url(base_url+str(i*25))
        soup = bf(html, "html.parser")
        for data in soup.find_all("div", class_="item"):
            sub_data = []
            data = str(data)
            moive_link = re.findall(MOIVE_LINK, data)[0]
            img_link = re.findall(IMG_LINK, data)[0]
            name = re.findall(NAME, data)[0]
            rate = re.findall(RATE, data)[0]
            judge = re.findall(JUDGE_NUM, data)[0]
            inq = re.findall(INQ, data)
            rank += 1
            if len(inq) != 0:
                inq = inq[0].replace("。", "")
            else:
                inq = " "
            sub_data.extend([name, rank, moive_link,
                            img_link, rate, judge, inq])
            data_list.append(sub_data)
    print("数据获取完成")
    return data_list


def save_xlws(save_path_name, data_list):
    work_book = xlwt.Workbook()
    work_sheet = work_book.add_sheet("TOP250")
    work_sheet.write(0, 0, "name")
    work_sheet.write(0, 1, "moive link")
    work_sheet.write(0, 2, "image link")
    work_sheet.write(0, 3, "rate")
    work_sheet.write(0, 4, "judge number")
    work_sheet.write(0, 5, "infomation")
    for index, data in enumerate(data_list):
        for j in range(len(data)):
            work_sheet.write(index+1, j, data[j])
    work_book.save(save_path_name)


def save_db(datas):
    db = SqlHelper()
    db.insert(datas=datas)


def ask_url(url):
    '''
    模拟浏览器登陆的信息,向服务器发送请求
    '''
    html = ""
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
    }
    req = request.Request(url, headers=head)

    try:
        res = request.urlopen(req, timeout=1)
        html = res.read().decode('utf-8')
    except error.URLError as e:
        if hasattr(e, "reason"):
            print(e.reason)
        if hasattr(e, "code"):
            print(e.code)
        sys.exit()
    return html


def main():
    base_url = "https://movie.douban.com/top250?start="
    data_list = get_data(base_url)
    save_db(data_list)


if __name__ == "__main__":
    main()
