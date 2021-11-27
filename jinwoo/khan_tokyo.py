import pandas as pd
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import re


user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                     'Chrome/96.0.4664.45 Safari/537.36'
headers = {'User-Agent': user_agent}


def make_href(href):
    pre = 'https://sports.khan.co.kr/'
    return pre + href


def get_all_article_href(max_page):
    href_list = []
    print('get all article href')
    for page_num in tqdm(range(1, max_page + 1)):
        url = 'https://sports.khan.co.kr/olympic/tokyo2020/list.html?page={}'.format(page_num)
        req = requests.get(url, headers=headers)
        soup = BeautifulSoup(req.text, 'html.parser')

        a_list = soup.select('#content > div.cont_left > div.listWrap > dl > dt > a')
        for a in a_list:
            href = make_href(a['href'])
            href_list.append(href)

    return href_list


def get_title(soup):
    title = soup.select_one('#article_title').text
    return title.strip()


def get_reporter(soup):
    reporter = soup.select_one('span.txt_name').text
    return reporter.strip()


def get_date(soup):
    date = soup.select_one('div.byline > em').text
    date = re.findall('\d{4} ?\. ?\d{1,2} ?\. ?\d{1,2}',date)[-1]
    return date.strip()


def get_contents(soup):
    p_list = soup.select('p.content_text')
    contents = []
    for p in p_list:
        contents.append(p.text.strip())
    return '\n'.join(contents)


if __name__ == '__main__':
    hrefs = get_all_article_href(92)

    except_list = []

    title_list = []
    date_list = []
    reporter_list = []
    contents_list = []
    print('crawling article')
    for href in tqdm(hrefs):
        try:
            req = requests.get(href, headers=headers)
            soup = BeautifulSoup(req.text, 'html.parser')

            title = get_title(soup)
            date = get_date(soup)
            reporter = get_reporter(soup)
            content = get_contents(soup)

            title_list.append(title)
            date_list.append(date)
            reporter_list.append(reporter)
            contents_list.append(content)
        except:
            except_list.append(href)

    df = pd.DataFrame({
        'title': title_list,
        'date': date_list,
        'reporter': reporter_list,
        'content': contents_list
    })

    df.to_csv('data.csv', index=False, encoding='utf-8-sig')

    except_df = pd.DataFrame({
        'href': except_list
    })

    except_df.to_csv('except.csv', index=False, encoding='utf-8-sig')