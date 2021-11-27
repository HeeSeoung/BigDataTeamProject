import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import re
from tqdm import tqdm


user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
             'Chrome/96.0.4664.45 Safari/537.36'
headers = {'User-Agent': user_agent}


def make_href(href):
    pre = 'https://www.seoul.co.kr/'
    return pre + href


def get_all_article_href(url):
    driver = webdriver.Chrome('../driver/chromedriver.exe')
    driver.get(url)

    while True:
        try:
            more_button = driver.find_element_by_xpath('/html/body/div[2]/div[6]/div/div[1]/div/div[2]/a/div')
            more_button.click()
        except:
            break

    time.sleep(2)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    a_list = soup.select('li.S20_List_article > div.thumb > a')

    href_list = []
    for a in a_list:
        href = make_href(a['href'])
        href_list.append(href)

    return href_list


def get_title(soup):
    title = soup.select_one('h1.atit2').text
    return title.strip()


def get_date(soup):
    date = soup.select_one('span.w_date').text
    date = re.findall('\d{4} ?[\.-] ?\d{1,2} ?[\.-] ?\d{1,2}', date)[-1]
    return date.strip()


def get_contents(soup):
    contents = soup.select_one('#atic_txt1').text
    return contents.strip()


if __name__ == '__main__':
    url = 'https://www.seoul.co.kr/news/newsList.php?section=Tokyo2020'
    href_list = get_all_article_href(url)

    except_list = []
    massage_list = []

    title_list = []
    date_list = []
    content_list = []
    for href in tqdm(href_list):
        try:
            req = requests.get(href, headers=headers)
            req.encoding = 'utf-8'
            soup = BeautifulSoup(req.text, 'html.parser')

            title = get_title(soup)
            date = get_date(soup)
            content = get_contents(soup)

            title_list.append(title)
            date_list.append(date)
            content_list.append(content)
        except Exception as e:
            except_list.append(href)
            massage_list.append(e)

    df = pd.DataFrame({
        'title': title_list,
        'date': date_list,
        'content': content_list
    })

    df.to_csv('data.csv', index=False, encoding='utf-8-sig')

    except_df = pd.DataFrame({
        'href': except_list,
        'massage': massage_list
    })

    except_df.to_csv('except.csv', index=False, encoding='utf-8-sig')