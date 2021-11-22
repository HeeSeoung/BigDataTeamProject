import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import re


search_date = 20210723   # 20210723 ~ 20210808
url = 'https://v.daum.net/v/20210724044700219'

req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')

p_list = soup.select('#harmonyContainer > section > p')
contents = []
for p in p_list:
    contents.append(p.text)
print('\n'.join(contents))