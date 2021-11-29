import pandas as pd
from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image
import numpy as np


def AddNouns(dataset) -> list:
    '''
    명사 추출 데이터를 데이터 프레입에 추가합니다.
    input : 'title', 'content' 포함된 dataframe
    output : dataframe
    '''
    nouns = []
    all = []
    for title, contents in zip(dataset['title'], dataset['content']):
        li = tagger.nouns(title)
        li.extend(tagger.nouns(contents))
        all.extend(li)
        nouns.append(li)

    dataset['nouns'] = nouns
    return all


dataset = pd.read_csv("../jinwoo/data/경향_도쿄.csv")
tagger = Okt()
dataset, all_nouns = AddNouns(dataset)

fontPath = './DoHyeon-Regular.ttf'
pictogram = np.array(Image.open('./basketball.jpeg'))

counts = Counter(all_nouns)
tags = counts.most_common(2000)

wc = WordCloud(font_path=fontPath,
               background_color="white",
               max_font_size=60,
               max_words=1000,
               )
cloud = wc.generate_from_frequencies(dict(tags))
cloud.to_file('./test.jpg')

# 데이터 전처리 : Labeling

eventList = ['3x3 농구', '양궁', '육상', '배드민턴', '농구', '사이클 BMX 프리스타일', '사이클 BMX 레이싱', '복싱', '야구 소프트볼', '스포츠클라이밍', '사이클 도로', '카누 슬라럼', '카누스프린트', '사이클', '사이클 트랙', '다이빙', '승마', '축구', '펜싱', '기계체조', '골프',
             '리듬체조', '트램펄린', '핸드볼', '하키', '유도', '가라테', '근대 5종', '사이클 MTB', '마라톤 수영', '조정', '럭비', '요트', '사격', '스케이트보드', '서핑', '아티스틱 스위밍', '수영', '테니스', '태권도', '트라이애슬론', '탁구', '비치발리볼', '배구', '역도', '수구', '레슬링']

label = []
titleList = []
contentList = []

for title, content, nouns in zip(dataset['title'], dataset['content'], dataset['nouns']):
    is_visited = [False for i in range(len(eventList))]
    for noun in nouns:
        for k in range(len(eventList)):
            if noun == eventList[k] and not is_visited[k]:
                is_visited[k] = True
                label.append(eventList[k])
                titleList.append(title)
                contentList.append(content)

data_revised = pd.DataFrame({
    'title': titleList,
    'content': contentList,
    'label': label
})
data_revised.to_csv('/content/drive/MyDrive/data/bigdata/test_list.csv')
