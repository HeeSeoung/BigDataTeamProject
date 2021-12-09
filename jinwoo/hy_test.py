from scipy.stats import ttest_ind
import pandas as pd


rio = pd.read_csv('./data/rio_athletes.csv')
tokyo = pd.read_csv('./data/tokyo_athletes.csv')

# tokyo = NOC
# rio = nationality
print(tokyo['NOC'].value_counts().mean())
print(rio['nationality'].value_counts().mean())


print(ttest_ind(tokyo['NOC'].value_counts(), rio['nationality'].value_counts()))