import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
from tqdm import tqdm
import pandas as pd


def word_count_bar(df_):
    df = df_.copy()

    counts = Counter()

    for noun in df['nouns'].tolist():
        counts.update(noun.split(','))

    most_words = counts.most_common(10)
    most_sr = most_common_to_sr(most_words)

    plt.figure(figsize=(12, 10))
    f = sns.barplot(x=most_sr.values, y=most_sr.index, alpha=0.8)
    f.set_facecolor('#d9eaff')
    f.grid(True, axis='y', alpha=0.5)
    f.set_title('단어 빈도 TOP 10')
    f.tick_params(axis='x', rotation=45)


def most_common_to_sr(most_common):
    most_dict = {i[0]: i[1] for i in most_common}
    sr = pd.Series(most_dict)

    return sr


def date_line_plot(data_, region):
    data = data_.copy()

    data['date'] = pd.to_datetime(data['date'])

    date_group = data.groupby('date')
    if region == 'tokyo':
        dates = pd.date_range('20210723', '20210808')
    else:
        dates = pd.date_range('20160805', '20160821')
    dates_sr = pd.Series(index=dates)

    for date in dates:
        try:
            date_df = date_group.get_group(date)
            dates_sr[date] = date_df.shape[0]
        except:
            dates_sr[date] = 0

    plt.figure(figsize=(12, 10))
    f = sns.lineplot(x=dates_sr.index, y=dates_sr.values, color='red', marker='o', alpha=0.8)
    f.set_facecolor('#d9eaff')
    f.grid(True, axis='x', alpha=0.5)
    f.set_title('날짜별 기사 갯수')
    plt.xticks(rotation=45)

    return f


def press_bar_plot(data_):
    data = data_.copy()

    press_sr = data['press'].value_counts()[:5]

    plt.figure(figsize=(10, 12))
    f = sns.barplot(x=press_sr.index, y=press_sr.values, alpha=0.8)
    f.set_facecolor('#d9eaff')
    f.grid(True, axis='y', alpha=0.5)
    f.tick_params(axis='x', rotation=45)
    f.set_title('언론사별 기사 갯수')

    return f


def main():
    df = '종목별로 묶인 데이터 프레임 ex) 농구만 있는 df'

    word_count_bar(df)  # 단어 빈도 그리기
    date_line_plot(df, 'tokyo')   # 날짜별 기사수 그리기, 리우인지 토쿄인지 알려줘야함
    # press_bar_plot(df)   # 언론사 별 기사수 그리기
