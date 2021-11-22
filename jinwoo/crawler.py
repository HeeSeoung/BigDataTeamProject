# Daum Sport news crawling
# 동적 웹 크롤링을 위해 셀레니움 사용
# made by jinwoo
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import re
import pandas as pd


# 기사 링크 획득 함수
# start_date : 기사 수집 시작 날짜
# end_date : 기사 수집 끝 날짜
def get_hrefs(start_date, end_date):
    search_date = start_date

    hrefs = []
    while search_date != (end_date + 1):
        url = 'https://sports.daum.net/news/ranking?date={}'.format(search_date)
        driver = webdriver.Chrome('../driver/chromedriver.exe')
        driver.get(url)
        time.sleep(0.1)

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        a_list = soup.select('strong.tit_news > a.link_txt')

        for a in a_list:
            hrefs.append(a['href'])
        search_date += 1
    return hrefs


# 기사 제목 획득
def get_title(soup):
    title = soup.select_one('h3.tit_view').text
    return title.strip()


# 기사 작성 날짜와 기자 획득
def get_date_and_reporter(soup):
    info_view = soup.select_one('span.info_view').text
    date = re.findall('\d{4} ?\. ?\d{1,2} ?\. ?\d{1,2}', info_view)[-1]   # 날짜 포맷의 정규표현식

    reporter = info_view.split('입력')[0]
    return date.strip(), reporter.strip()


# 언론사 획득
def get_press(soup):
    press = soup.select_one('em > a > img.thumb_g')['alt']
    return press.strip()


# 기사 내용 획득
def get_contents(soup):
    p_list = soup.select('#harmonyContainer > section > p')
    contents = []
    for p in p_list:
        contents.append(p.text)
    return '\n'.join(contents).strip()   # 문단을 개행으로 연결


# tokyo : 20210723 ~ 20210808
if __name__ == '__main__':
    start_date = 20210723
    end_date = 20210808
    hrefs = get_hrefs(start_date, end_date)   # 기사 링크들 획득

    title_list = []   # 제목을 담을 리스트
    date_list = []   # 날짜를 담을 리스트
    reporter_list = []   # 기자를 담을 리스트
    press_list = []   # 언론사를 담을 리스트
    content_list = []   # 본문을 담을 리스트
    for href in hrefs:
        req = requests.get(href)   # 기사 링크 GET 요청
        soup = BeautifulSoup(req.text, 'html.parser')   # html parsing

        # 각 요소들을 획득
        title = get_title(soup)
        date, reporter = get_date_and_reporter(soup)
        press = get_press(soup)
        content = get_contents(soup)

        # 각 요소들을 리스트에 append
        title_list.append(title)
        date_list.append(date)
        reporter_list.append(reporter)
        press_list.append(press)
        content_list.append(content)

    # DataFrame 생성
    df = pd.DataFrame({
        'title': title_list,
        'date': date_list,
        'reporter': reporter_list,
        'press': press_list,
        'contents': content_list
    })

    # csv 저장
    # 제목은 수집 시작 날짜_종료 날짜로 설정(구분을 위해)
    df.to_csv(str(start_date) + '_' + str(end_date) + '.csv', index=False, encoding='utf-8-sig')
