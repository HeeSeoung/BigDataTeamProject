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

    sns.barplot(x=most_sr.values, y=most_sr.index, alpha=0.8)
    plt.gca().set_facecolor('#d9eaff')
    plt.grid(True, axis='x', alpha=0.5)
    plt.title('단어 빈도 Top 10')
    plt.show()


def most_common_to_sr(most_common):
    most_dict = {i[0]: i[1] for i in most_common}
    sr = pd.Series(most_dict)

    return sr