import pandas as pd
from konlpy.tag import Okt
from sklearn.feature_extraction.text import CountVectorizer


def make_dtm(df_):
    df = df_.copy()

    cv = CountVectorizer(token_pattern='[가-힣a-zA-Z0-9]+')
    DTM_Array = cv.fit_transform(df['nouns'])
    feature_names = cv.get_feature_names()
    DTM_DataFrame = pd.DataFrame(DTM_Array, columns=feature_names)

    return DTM_DataFrame


df = pd.read_csv('./data/sample.csv')
temp = make_dtm(df)
print(temp)





