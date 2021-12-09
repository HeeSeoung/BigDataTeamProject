import pandas as pd
import chart_studio.plotly as py
import cufflinks as cf
cf.go_offline(connected=True)

data = pd.read_csv('../data/dataset_olympics(20211207)', index_col=0)

# date 컬럼 추가
date = []
for i in zip(data['Olympic']):
  date.append(int(i[0].split('-')[-1]))

print(date)
data['date'] = date

# 일본의 올림픽 결과를 시간순으로 추출
data = data.sort_values('date', ascending=True)
data_japan = data[data['Nation'] == 'Japan']

# 그래프 확인
df = cf.datagen.lines()
df.head()

df.iplot(kind='line')

