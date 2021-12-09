from konlpy.tag import Okt
import pandas as pd


stop_words = pd.read_csv('./stopwords.txt', header=None)[0].tolist()


def preprocessing(df_, path):
    df = df_.copy()

    df['date'] = pd.to_datetime(df['date'])
    df['Noun'] = df['content'].apply(pos_filter)

    # tokyo: 20210723 ~ 20210808
    if '도쿄' in path:
        mask = (df['date'] >= pd.to_datetime('20210723')) & (df['date'] <= pd.to_datetime('20210808'))
        df = df[mask]
    # rio : 20160805 ~ 20160821
    else:
        mask = (df['date'] >= pd.to_datetime('20160805')) & (df['date'] <= pd.to_datetime('20160821'))
        df = df[mask]

    return df


def pos_filter(x):
    pos_list = Okt().pos(x)
    nouns = [word for word, pos in pos_list if pos == 'Noun' and word not in stop_words and len(word) != 1]
    return ','.join(nouns)
