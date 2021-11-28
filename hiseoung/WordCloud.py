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
