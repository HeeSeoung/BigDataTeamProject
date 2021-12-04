import pandas as pd
from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image
import numpy as np
import re
from datetime import datetime
fontPath = './resources/font/DoHyeon-Regular.ttf'
img_path = './resources/pictogram'
save_path = './resources/wordcloud'

def makeWC(dataset, label) -> str:
    '''
    전처리가 완료된 데이터프레임과 레이블값을 입력받아 해당 종목의 워드 클라우드를 생성합니다.
    input : 'title', 'content', 'date', 'nouns', 'label' 포함된 dataframe
    output : 업로드 파일 경로
    '''

    pictogram = np.array(Image.open(f'{img_path}/{label}.jpg'))
    condition = (dataset.label == label)
    dataset = dataset[condition]
    all_nouns = []

    for i in zip(dataset['nouns']):
        for j in i:
            all_nouns.extend(j)

    text = [x for x in all_nouns if len(x) > 1]
    counts = Counter(text)
    tags = counts.most_common(20000)
    wc = WordCloud(font_path=fontPath,
                   background_color="white",
                   max_font_size=300,
                   max_words=20000,
                   mask = pictogram
                   )
    path = f'{save_path}/{label}.jpg'
    cloud = wc.generate_from_frequencies(dict(tags))
    cloud.to_file(path)

