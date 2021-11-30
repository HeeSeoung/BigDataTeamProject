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


def most_common_to_sr(most_common):
    most_dict = {i[0]: i[1] for i in most_common}
    sr = pd.Series(most_dict)

    return sr