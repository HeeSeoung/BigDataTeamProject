import pandas as pd
from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image
import numpy as np
import re
from datetime import datetime

def wordCloud(dataset, label) -> str:
    '''
    전처리가 완료된 데이터프레임과 레이블값을 입력받아 해당 종목의 워드 클라우드를 생성합니다.
    input : 'title', 'content', 'date', 'nouns', 'label' 포함된 dataframe
    output : 업로드 파일 경로
    '''

    fontPath = './DoHyeon-Regular.ttf'
    pictogram = np.array(Image.open(f'./{label}.jpeg'))

    condition = (dataset.label == label)
    dataset = dataset[condition]
    all_nouns = []

    for i in zip(dataset['nouns']):
        all_nouns.extend(i)

    text = [x for x in all_nouns if len(x) > 1]

    counts = Counter(text)
    tags = counts.most_common(20000)

    wc = WordCloud(font_path=fontPath,
                   background_color="white",
                   max_font_size=300,
                   max_words=20000,
                   mask = pictogram
                   )

    # 폴더 이름 설정 : 업로드한 시간(밀리세컨드)
    t = re.findall("\d+", datetime.now().isoformat(timespec='milliseconds'))
    upload_time = ''.join(t)

    path = f'./{upload_time}.jpg'
    cloud = wc.generate_from_frequencies(dict(tags))
    cloud.to_file(path)

    return path


