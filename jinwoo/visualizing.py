import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
from tqdm import tqdm
import pandas as pd


def word_count_bar(df_):
    df = df_.copy()

    counts = Counter()

    for noun in df['Noun'].tolist():
        counts.update(noun.split(','))

    most_words = counts.most_common(10)
    most_sr = most_common_to_sr(most_words)

    plt.figure(figsize=(12, 10))
    sns.barplot(x=most_sr.values, y=most_sr.index, alpha=0.8)
    plt.gca().set_facecolor('#d9eaff')
    plt.grid(True, axis='x', alpha=0.5)
    plt.title('단어 빈도 Top 10')
    plt.show()


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
    plt.title('기사 갯수')
    sns.lineplot(x=dates_sr.index, y=dates_sr.values, color='red', marker='o', alpha=0.8)
    plt.gca().set_facecolor('#d9eaff')
    plt.grid(True, axis='x', alpha=0.5)
    plt.xticks(rotation=45)


def press_bar_plot(data_):
    data = data_.copy()

    press_sr = data['press'].value_counts()[:5]

    plt.figure(figsize=(10, 12))
    sns.barplot(x=press_sr.index, y=press_sr.values, alpha=0.8)
    plt.gca().set_facecolor('#d9eaff')
    plt.grid(True, axis='y', alpha=0.5)
    plt.xticks(rotation=45)
    plt.title('언론사별 기사 갯수')
    plt.show()

