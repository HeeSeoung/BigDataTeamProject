import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def top_line_gold(data_):
    data = data_.copy()

    # data 처리 부분. 하계 올림픽과 도쿄 올림픽 기준 Top 5 국가만 남김김
    summer_mask = data['type'] == 'summer'
    summer = data[summer_mask]

    ROC = summer['Nation'] == 'ROC'
    summer.loc[ROC, 'Nation'] = 'Russian Federation'

    top_5 = ['United States of America', 'People\'s Republic of China', 'Russian Federation', 'Great Britain', 'Japan']

    mask = summer['Nation'].isin(top_5)
    top_5_summer = summer[mask]

    group = top_5_summer.groupby('Nation')

    f = plt.figure(figsize=(12, 10))
    ax = f.add_subplot(1, 1, 1)
    for name in top_5:
        df = group.get_group(name)
        sns.lineplot(data=df, x='year', y='Gold', marker='o', label=name, ax=ax)
    ax.set_xticks(list(range(1996, 2021, 4)))
    ax.grid()
    ax.set_title('TOP 5 / GOLD medals', size=15)

    return f


def top_line_rank(data_):
    data = data_.copy()

    summer_mask = data['type'] == 'summer'
    summer = data[summer_mask]

    ROC = summer['Nation'] == 'ROC'
    summer.loc[ROC, 'Nation'] = 'Russian Federation'

    top_5 = ['United States of America', 'People\'s Republic of China', 'Russian Federation', 'Great Britain', 'Japan']

    mask = summer['Nation'].isin(top_5)
    top_5_summer = summer[mask]

    group = top_5_summer.groupby('Nation')

    f = plt.figure(figsize=(12, 10))
    ax = f.add_subplot(1, 1, 1)
    for name in top_5:
        df = group.get_group(name)
        sns.lineplot(data=df, x='year', y='rank', marker='o', label=name, ax=ax)
    ax.set_xticks(list(range(1996, 2021, 4)))
    ax.grid()
    ax.set_title('TOP 5 / Ranking', size=15)

    return f


def top_line_total(data_):
    data = data_.copy()

    summer_mask = data['type'] == 'summer'
    summer = data[summer_mask]

    ROC = summer['Nation'] == 'ROC'
    summer.loc[ROC, 'Nation'] = 'Russian Federation'

    top_5 = ['United States of America', 'People\'s Republic of China', 'Russian Federation', 'Great Britain', 'Japan']

    mask = summer['Nation'].isin(top_5)
    top_5_summer = summer[mask]

    group = top_5_summer.groupby('Nation')

    f = plt.figure(figsize=(12, 10))
    ax = f.add_subplot(1,1,1)
    for name in top_5:
        df = group.get_group(name)
        sns.lineplot(data=df, x='year', y='total_rank', marker='o', label=name, ax=ax)
    ax.set_xticks(list(range(1996, 2021, 4)))
    ax.grid()
    ax.set_title('TOP 5 / Total Ranking', size=15)

    return f


def pie_chart_gold(data_):
    data = data_.copy()

    summer_mask = data['type'] == 'summer'
    summer = data[summer_mask]

    ROC = summer['Nation'] == 'ROC'
    summer.loc[ROC, 'Nation'] = 'Russian Federation'

    top_5 = ['United States of America', 'People\'s Republic of China', 'Russian Federation', 'Great Britain', 'Japan']

    mask = summer['Nation'].isin(top_5)
    top_5_summer = summer[mask]

    tokyo = top_5_summer[top_5_summer['Olympic'] == 'tokyo-2020']
    f = plt.figure(figsize=(12, 12))
    ax = f.add_subplot(1, 1, 1)
    ax.pie(tokyo['Gold'],
           labels=top_5,
           autopct=lambda p: '{:.0f}'.format(p * sum(tokyo['Gold']) / 100),
           textprops={'fontsize': 12})
    ax.set_title('Top 5 Gold medals', size=20)

    return f


def pie_chart_total(data_):
    data = data_.copy()

    summer_mask = data['type'] == 'summer'
    summer = data[summer_mask]

    ROC = summer['Nation'] == 'ROC'
    summer.loc[ROC, 'Nation'] = 'Russian Federation'

    top_5 = ['United States of America', 'People\'s Republic of China', 'Russian Federation', 'Great Britain', 'Japan']

    mask = summer['Nation'].isin(top_5)
    top_5_summer = summer[mask]

    tokyo = top_5_summer[top_5_summer['Olympic'] == 'tokyo-2020']
    f = plt.figure(figsize=(12, 12))
    ax = f.add_subplot(1, 1, 1)
    ax.pie(tokyo['total'],
           labels=top_5,
           autopct=lambda p: '{:.0f}'.format(p * sum(tokyo['total']) / 100),
           textprops={'fontsize': 12})
    ax.set_title('Top 5 total medals', size=20)

    return f


def home_advantage_gold(data_):
    data = data_.copy()

    summer_mask = data['type'] == 'summer'
    summer = data[summer_mask]

    ROC = summer['Nation'] == 'ROC'
    summer.loc[ROC, 'Nation'] = 'Russian Federation'

    top_5 = ['United States of America', 'People\'s Republic of China', 'Russian Federation', 'Great Britain', 'Japan']

    mask = summer['Nation'].isin(top_5)
    top_5_summer = summer[mask]

    top_5_summer['host'] = 'N'

    atlanta = (top_5_summer['Olympic'] == 'atlanta-1996') & (top_5_summer['Nation'] == 'United States of America')
    beijing = (top_5_summer['Olympic'] == 'beijing-2008') & (top_5_summer['Nation'] == 'People\'s Republic of China')
    london = (top_5_summer['Olympic'] == 'london-2012') & (top_5_summer['Nation'] == 'Great Britain')
    tokyo = (top_5_summer['Olympic'] == 'tokyo-2020') & (top_5_summer['Nation'] == 'Japan')

    top_5_summer.loc[atlanta, 'host'] = 'Y'
    top_5_summer.loc[beijing, 'host'] = 'Y'
    top_5_summer.loc[london, 'host'] = 'Y'
    top_5_summer.loc[tokyo, 'host'] = 'Y'

    No_df = top_5_summer[top_5_summer['host'] == 'N']
    y_df = top_5_summer[top_5_summer['host'] == 'Y']
    temp = No_df.groupby('Nation')[['Gold', 'Silver', 'Bronze']].mean()
    temp['Nation'] = temp.index
    temp['host'] = 'N'
    temp = temp.reset_index(drop=True)
    temp2 = y_df[['Gold', 'Silver', 'Bronze', 'Nation', 'host']]
    com = pd.concat([temp, temp2])
    com = com[com['Nation'] != 'Russian Federation']
    com['total'] = com.apply(lambda x: x['Gold'] + x['Silver'] + x['Bronze'], axis=1)

    f = plt.figure(figsize=(12, 10))
    ax = f.add_subplot(1, 1, 1)
    sns.barplot(data=com, x='Nation', y='Gold', hue='host', ax=ax)
    ax.bar_label(ax.containers[0])
    ax.bar_label(ax.containers[1])
    ax.set_title('host VS None host Gold medals', fontsize=15)

    return f


def home_advantage_total(data_):
    data = data_.copy()

    summer_mask = data['type'] == 'summer'
    summer = data[summer_mask]

    ROC = summer['Nation'] == 'ROC'
    summer.loc[ROC, 'Nation'] = 'Russian Federation'

    top_5 = ['United States of America', 'People\'s Republic of China', 'Russian Federation', 'Great Britain', 'Japan']

    mask = summer['Nation'].isin(top_5)
    top_5_summer = summer[mask]

    top_5_summer['host'] = 'N'

    atlanta = (top_5_summer['Olympic'] == 'atlanta-1996') & (top_5_summer['Nation'] == 'United States of America')
    beijing = (top_5_summer['Olympic'] == 'beijing-2008') & (top_5_summer['Nation'] == 'People\'s Republic of China')
    london = (top_5_summer['Olympic'] == 'london-2012') & (top_5_summer['Nation'] == 'Great Britain')
    tokyo = (top_5_summer['Olympic'] == 'tokyo-2020') & (top_5_summer['Nation'] == 'Japan')

    top_5_summer.loc[atlanta, 'host'] = 'Y'
    top_5_summer.loc[beijing, 'host'] = 'Y'
    top_5_summer.loc[london, 'host'] = 'Y'
    top_5_summer.loc[tokyo, 'host'] = 'Y'

    No_df = top_5_summer[top_5_summer['host'] == 'N']
    y_df = top_5_summer[top_5_summer['host'] == 'Y']
    temp = No_df.groupby('Nation')[['Gold', 'Silver', 'Bronze']].mean()
    temp['Nation'] = temp.index
    temp['host'] = 'N'
    temp = temp.reset_index(drop=True)
    temp2 = y_df[['Gold', 'Silver', 'Bronze', 'Nation', 'host']]
    com = pd.concat([temp, temp2])
    com = com[com['Nation'] != 'Russian Federation']
    com['total'] = com.apply(lambda x: x['Gold'] + x['Silver'] + x['Bronze'], axis=1)

    f = plt.figure(figsize=(10, 14))
    ax = f.add_subplot(1, 1, 1)
    sns.barplot(data=com, x='Nation', y='total', hue='host', ax=ax)
    ax.bar_label(ax.containers[0])
    ax.bar_label(ax.containers[1])
    ax.set_title('host VS None host Total medals', size=15)

    return f