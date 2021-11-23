# Daum Sport news crawling
# 동적 웹 크롤링을 위해 셀레니움 사용
# made by jinwoo
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import re
import pandas as pd
from tqdm import tqdm


# 유효링크로 만들어 줌
def make_query(href):
    prefix = 'https://sports.news.naver.com/news?'
    href = href.split('?')[-1]

    return prefix + href


# 기사 링크 획득 함수
# start_date : 기사 수집 시작 날짜
# end_date : 기사 수집 끝 날짜
def get_hrefs(start_date, end_date):
    search_dates = pd.date_range(start_date, end_date).strftime('%Y%m%d').tolist()   # get date

    hrefs = []
    print('get hrefs')
    for search_date in tqdm(search_dates):
        url = 'https://sports.news.naver.com/ranking/index.nhn?date={}'.format(search_date)
        driver = webdriver.Chrome('../driver/chromedriver.exe')
        driver.get(url)
        time.sleep(2)

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        a_list = soup.select('div.content_area > div > ul > li > div.text > a.title')
        for a in a_list:
            href = make_query(a['href'])
            hrefs.append(href)
    return hrefs


# 기사 제목 획득
def get_title(soup):
    title = soup.select_one('h4.title').text
    return title.strip()


# 기사 작성 날짜 획득
def get_date(soup):
    info_view = soup.select_one('div.info').text
    date = re.findall('\d{4} ?\. ?\d{1,2} ?\. ?\d{1,2}', info_view)[-1]   # 날짜 포맷의 정규표현식

    return date.strip()


# 기자 획득
def get_reporter(soup):
    reporter = soup.select_one('p.byline').text
    return reporter.strip()


# 언론사 획득
def get_press(soup):
    press = soup.select_one('span.logo > a.link > img')['alt']
    return press.strip()


# 기사 내용 획득
def get_contents(soup):
    content = soup.select_one('#newsEndContents').text
    return content.strip()


# tokyo : 20210723 ~ 20210808
# rio : 20160805 ~ 20160821
if __name__ == '__main__':
    start_date = '20210723'
    end_date = '20210808'
    hrefs = get_hrefs(start_date, end_date)   # 기사 링크들 획득

    print('the number of articles :', len(hrefs))
    title_list = []   # 제목을 담을 리스트
    date_list = []   # 날짜를 담을 리스트
    reporter_list = []   # 기자를 담을 리스트
    press_list = []   # 언론사를 담을 리스트
    content_list = []   # 본문을 담을 리스트
    for href in tqdm(hrefs):
        try:
            req = requests.get(href)   # 기사 링크 GET 요청
            soup = BeautifulSoup(req.text, 'html.parser')   # html parsing

            # 각 요소들을 획득
            title = get_title(soup)
            date = get_date(soup)
            reporter = get_reporter(soup)
            press = get_press(soup)
            content = get_contents(soup)
        except Exception as e:
            continue

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
