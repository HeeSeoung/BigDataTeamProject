from scipy.stats import pearsonr
import pandas as pd


data = pd.read_csv('./data/tokyo_corona (1).csv')
data['Case-Fatality'] = data['Case-Fatality'].apply(lambda x: float(x.replace('%', '')))
# print(data.info())
cor = pearsonr(data['Gold'], data['Case-Fatality'])

print(cor)