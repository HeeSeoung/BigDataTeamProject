import pandas as pd
import os

os.chdir('/Users/hiseoung/PycharmProjects/pythonProject/BigDataTeamProject/hiseoung')

athletes = pd.read_csv('../data/olympic_all/olympic_athletes.csv')
hosts = pd.read_csv('../data/olympic_all/olympic_hosts.csv')
medals = pd.read_csv('../data/olympic_all/olympic_medals.csv')
results = pd.read_csv('../data/olympic_all/olympic_results.csv')
