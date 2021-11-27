import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import re


url = 'https://stv.seoul.co.kr/news/newsView.php?id=20160822500102'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
             'Chrome/96.0.4664.45 Safari/537.36'
headers = {'User-Agent': user_agent}
req = requests.get(url, headers=headers)   # 기사 링크 GET 요청
req.encoding = 'utf-8'
soup = BeautifulSoup(req.text, 'html.parser')   # html parsing

temp = soup.select_one('div.Vtit_box > p > span')
print(temp.text.strip())