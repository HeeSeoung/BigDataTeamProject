import pandas as pd
from konlpy.tag import Okt
import numpy as np


def AddNouns(dataset) -> pd.DataFrame:
    '''
    명사 추출 데이터를 데이터 프레입에 추가합니다.
    input : 'title', 'content', 'date' 포함된 dataframe
    output : dataframe
    '''
    nouns = []
    all = []

    tagger = Okt()

    for title, contents in zip(dataset['title'], dataset['content']):
        li = tagger.nouns(title)
        li.extend(tagger.nouns(contents))
        all.extend(li)
        nouns.append(li)

    dataset['nouns'] = nouns
    return dataset


def textPreprocessing(dataset) -> pd.DataFrame:
    '''
    입력받은 데이터 프레임에 레이블을 추가합니다.
    input : 'title', 'content', 'date', 'nouns' 포함된 dataframe
    output : dataframe
    '''

    eventList = ['3x3 농구', '양궁', '육상', '배드민턴', '농구', '사이클 BMX 프리스타일', '사이클 BMX 레이싱', '복싱', '야구 소프트볼',
                 '스포츠클라이밍', '사이클 도로', '카누 슬라럼', '카누스프린트', '사이클', '사이클 트랙', '다이빙', '승마', '축구', '펜싱',
                 '기계체조', '골프', '리듬체조', '트램펄린', '핸드볼', '하키', '유도', '가라테', '근대 5종', '사이클 MTB', '마라톤 수영',
                 '조정', '럭비', '요트', '사격', '스케이트보드', '서핑', '아티스틱 스위밍', '수영', '테니스', '태권도', '트라이애슬론',
                 '탁구', '비치발리볼', '배구', '역도', '수구', '레슬링']
    label = []
    titleList = []
    contentList = []
    nounsList = []
    dateList = []

    for title, content, nouns, date in zip(dataset['title'], dataset['content'], dataset['nouns'], dataset['date']):
      is_visited = [False for i in range(len(eventList))]
      for noun in nouns:
        for k in range(len(eventList)):
          if noun == eventList[k] and not is_visited[k]:
            is_visited[k] = True
            label.append(eventList[k])
            titleList.append(title)
            contentList.append(content)
            nounsList.append(nouns)
            dateList.append(date)

    data_revised = pd.DataFrame({
        'title': titleList,
        'content': contentList,
        'label': label,
        'nouns': nounsList,
        'date': dateList
    })

    return data_revised