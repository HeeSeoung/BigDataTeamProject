import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import re


url = 'https://sports.news.naver.com/news?oid=117&aid=0002797688'
req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')

title = soup.select_one('p.byline')
print(title.text)