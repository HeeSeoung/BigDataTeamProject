import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import pandas as pd
import seaborn as sns

# 그래프 세팅
'''
1페이지 > 
   1) 도쿄올림픽 Top5 국가의 역대 올림픽 성적
    >> lineplot
   2) 도쿄올림픽 메달 수 >> 원 차트
   3) 홈버프 성적, 평균 성적 >> 막대그래프

2페이지 >
   1) 감염률 (감염자 수 / 전체 인구 *100)
   2) 치명률 
   3) 감염률 치명률, 금, 메달수 상관 분석 표

3페이지 > 
   1) GDP 순위
   2) GDP, 금메달, 메달 수 상관분석표
'''
matplotlib.rcParams.update({'font.size': 1})
dataset1 = pd.read_csv("resources/data/data_gdp.csv")
dataset2 = pd.read_csv("resources/data/tokyo_corona1050.csv")
# dataset3 = pd.read_csv("resources/data/corona_plot.csv").iloc[10:].reset_index(drop = True)
dataset4 = pd.read_csv('resources/data/olympic.csv')

dataset5 = pd.read_csv('resources/data/fatal_10.csv')
dataset6 = pd.read_csv('resources/data/confirmed_10.csv')

def setGraph1_1(color_pallete):
    data = dataset4.copy()

    summer_mask = data['type'] == 'summer'
    summer = data[summer_mask]

    ROC = summer['Nation'] == 'ROC'
    summer.loc[ROC, 'Nation'] = 'Russian Federation'

    top_5 = ['United States of America', 'People\'s Republic of China', 'Russian Federation', 'Great Britain',
             'Japan']

    mask = summer['Nation'].isin(top_5)
    top_5_summer = summer[mask]

    tokyo = top_5_summer[top_5_summer['Olympic'] == 'tokyo-2020']
    fig, ax = plt.subplots(figsize=(6, 6))
    fig.set_facecolor(color_pallete['bg_color'])

    ax.set_facecolor(color_pallete['bg_color_sub2'])
    ax.legend()
    patches, texts, pcts = ax.pie(
        tokyo['total'], labels=top_5,
        wedgeprops={'linewidth': 3.0, 'edgecolor': color_pallete['bg_color']},
        autopct=lambda p: '{:.0f}'.format(p * sum(tokyo['total']) / 100),
        textprops={'fontsize': 12, 'color':color_pallete['bg_color_sub2']})
    # Style just the percent values.
    plt.setp(pcts, color=color_pallete['bg_color_sub1'], fontweight='bold')
    ax.set_title('Top 5 total medals', fontsize=14, color = color_pallete['text_color'])

    canvas = FigureCanvas(fig)
    canvas.draw()
    return canvas


def setGraph1_2(color_pallete):
    data = dataset4.copy()

    summer_mask = data['type'] == 'summer'
    summer = data[summer_mask]

    ROC = summer['Nation'] == 'ROC'
    summer.loc[ROC, 'Nation'] = 'Russian Federation'

    top_5 = ['United States of America', 'People\'s Republic of China', 'Russian Federation', 'Great Britain',
             'Japan']

    mask = summer['Nation'].isin(top_5)
    top_5_summer = summer[mask]

    top_5_summer['host'] = 'N'

    atlanta = (top_5_summer['Olympic'] == 'atlanta-1996') & (top_5_summer['Nation'] == 'United States of America')
    beijing = (top_5_summer['Olympic'] == 'beijing-2008') & (
                top_5_summer['Nation'] == 'People\'s Republic of China')
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

    # 그래프 그리기

    f = plt.figure(figsize=(12, 10))
    f.set_facecolor(color_pallete['bg_color'])
    ax = f.add_subplot(1, 1, 1)
    ax.set_facecolor(color_pallete['bg_color_sub1'])
    sns.barplot(data=com, x='Nation', y='Gold', hue='host', ax=ax,palette=[color_pallete['sub_color'],color_pallete['main_color']],errwidth=0.5)
    ax.bar_label(ax.containers[0], fontsize= 10, color=color_pallete['bg_color_sub2'])
    ax.bar_label(ax.containers[1], fontsize= 10, color=color_pallete['bg_color_sub2'])
    ax.set_title('HOST VS None-HOST Gold medals', fontsize=12, color=color_pallete['text_color'])
    prop = dict(
        style='italic',  # 글씨 형식 - 이탤릭형식
        size=6  # 글씨 크기
    )
    config_legend = dict(  ## 범례 설정
        loc='upper left',  # 범례 위치 설정
        prop=prop  # 범례 폰트 속성
    )
    ax.legend(**config_legend)
    plt.xticks(fontsize = 8, color = color_pallete['text_color'])
    plt.yticks(fontsize=8, color=color_pallete['text_color'])
    ax.yaxis.label.set_size(10)
    ax.yaxis.label.set_color(color_pallete['text_color'])
    ticK_color = color_pallete['bg_color_sub1']
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_color(ticK_color)
    ax.spines['bottom'].set_color(ticK_color)
    canvas = FigureCanvas(f)
    canvas.draw()
    return canvas

def setGraph1_3(color_pallete):
    data = dataset4.copy()

    # data 처리 부분. 하계 올림픽과 도쿄 올림픽 기준 Top 5 국가만 남김김
    summer_mask = data['type'] == 'summer'
    summer = data[summer_mask]

    ROC = summer['Nation'] == 'ROC'
    summer.loc[ROC, 'Nation'] = 'Russian Federation'

    top_5 = ['United States of America', 'People\'s Republic of China', 'Russian Federation', 'Great Britain',
             'Japan']

    mask = summer['Nation'].isin(top_5)
    top_5_summer = summer[mask]

    group = top_5_summer.groupby('Nation')

    f = plt.figure(figsize=(12, 10))
    f.set_facecolor(color_pallete['bg_color'])
    ax = f.add_subplot(1, 1, 1)
    for name in top_5:
        df = group.get_group(name)
        sns.lineplot(data=df, x='year', y='Gold', label=name, ax=ax)

    plt.yticks([0, 10, 20, 30, 40, 50], fontsize=8, color=color_pallete['text_color'])
    plt.xticks(list(range(1996, 2021, 4)), fontsize=10, color=color_pallete['text_color'])
    ax.set_facecolor(color_pallete['bg_color_sub1'])
    prop = dict(
        style='italic',  # 글씨 형식 - 이탤릭형식
        size=6  # 글씨 크기
    )
    config_legend = dict(  ## 범례 설정
        loc='lower right',  # 범례 위치 설정
        prop=prop  # 범례 폰트 속성
    )

    ax.legend(**config_legend)
    ax.grid(color=color_pallete['bg_color'])
    ticK_color = color_pallete['bg_color_sub1']
    ax.set_title('TOP 5 / GOLD medals', fontsize=12, color=color_pallete['text_color'])
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_color(ticK_color)
    ax.spines['bottom'].set_color(ticK_color)

    canvas = FigureCanvas(f)
    canvas.draw()
    return canvas







# 도쿄, 치명률 감염률 상관계수... 이거 교체

def setGraph2_1(color_pallete):
    fig = plt.figure(figsize=(10, 10))
    fig.set_facecolor(color_pallete['bg_color'])
    ax = plt.gca()
    ax.set_facecolor(color_pallete['bg_color'])
    plt.title('Confirmed Rate', fontsize=10, color=color_pallete['text_color'])
    nations = dataset6['Nation'][::-1]
    values = dataset6['Confirmed/Pop'][::-1]
    ticK_color = color_pallete['bg_color_sub2']
    # 가로로 긴그래프 위, 사이드 축제거 spines = 축
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    ax.spines['left'].set_color(ticK_color)
    ax.spines['bottom'].set_color(ticK_color)
    ax.tick_params(axis='y', colors=ticK_color)
    ax.tick_params(axis='x', colors=ticK_color)
    y = np.arange(len(dataset6))
    plt.barh(y, values, color=color_pallete['main_color'], height=0.6)
    plt.yticks(y, nations, fontsize=9, color=color_pallete['text_color'])
    plt.xticks([0, 0.05, 0.1, 0.15, 0.2], fontsize=6, color=color_pallete['text_color'])

    canvas = FigureCanvas(fig)
    canvas.draw()
    return canvas


def setGraph2_2(color_pallete):
    fig = plt.figure(figsize=(10, 10))
    fig.set_facecolor(color_pallete['bg_color'])
    ax = plt.gca()
    ax.set_facecolor(color_pallete['bg_color'])
    plt.title('Fatality', fontsize=10, color=color_pallete['text_color'])

    nations = dataset5['Nation'][::-1]
    values = dataset5['Case-Fatality'][::-1]
    ticK_color = color_pallete['bg_color_sub2']
    # 가로로 긴그래프 위, 사이드 축제거 spines = 축
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    ax.spines['left'].set_color(ticK_color)
    ax.spines['bottom'].set_color(ticK_color)
    ax.tick_params(axis='y', colors=ticK_color)
    ax.tick_params(axis='x', colors=ticK_color)
    y = np.arange(len(dataset5))
    plt.barh(y, values, color=color_pallete['sub_color'], height=0.6)
    plt.yticks(y, nations, fontsize=9, color=color_pallete['text_color'])

    plt.xticks(list(range(0,21,5)), fontsize=6, color=color_pallete['text_color'])

    canvas = FigureCanvas(fig)
    canvas.draw()
    return canvas


def setGraph2_3(color_pallete):
    tokyo_corr = dataset2[['Gold', 'event_count', 'Case-Fatality', 'Death/100L Pop']]
    feature = ['Gold', 'event_count', 'Case-Fatality', 'Death/100L Pop']
    corr_feture = tokyo_corr.corr()
    fig = plt.figure(figsize=(6, 6))

    # 배경색바꾸기
    fig.set_facecolor(color_pallete['bg_color'])
    matplotlib.rcParams['text.color'] = color_pallete['text_color']
    n_feature = len(feature)
    for i in range(n_feature):
        for j in range(n_feature):
            ax = fig.add_subplot(n_feature, n_feature, i * n_feature + j + 1)


            # 안에 있는 subplot 배경색 바꾸기

            ax.set_facecolor(color_pallete['bg_color_sub1'])
            plt.scatter(feature[j], feature[i], data=tokyo_corr, s=1, color=color_pallete['main_color'], )
            # 축없애기
            remove_spines(plt)
            # x,y축 텍스트 변경
            ax.xaxis.label.set_color(color_pallete['bg_color_sub2'])
            ax.yaxis.label.set_color(color_pallete['bg_color_sub2'])

            if i == n_feature - 1:
                plt.xlabel(feature[j], fontsize=10)
            if j == 0:
                plt.ylabel(feature[i], fontsize=6)
            ax.annotate(np.round(corr_feture.loc[feature[i], feature[j]], 3), xy=(1, 0),
                        xycoords='axes fraction', fontsize=8,
                        horizontalalignment='right', verticalalignment='bottom')
    canvas = FigureCanvas(fig)
    canvas.draw()
    return canvas


# (완료)
def setGraph3_1(color_pallete):
    # GDP 2020년 기준
    sample = pd.DataFrame({
        'Nation': ['United States', 'China', 'Japan', 'Germany', 'United Kingdom', 'India', 'France', 'Italy', 'Canada',
                   'Korea'],
        'Value': [20893.75, 14866.74, 5045.10, 3843.34, 2709.68, 2660.24, 2624.42, 1884.94, 1644.04, 1638.26]
    })
    sample = sample.sort_values(by='Value', ascending=False)

    fig = plt.figure(figsize=(10, 10))
    fig.set_facecolor(color_pallete['bg_color'])

    ax = plt.gca()
    ax.set_facecolor(color_pallete['bg_color'])

    nations = sample['Nation']
    values = sample['Value']

    y = np.arange(len(sample))
    plt.bar(y, values, color=color_pallete['main_color'], width=0.6)
    plt.title('GDP Rank', fontsize=15, color=color_pallete['text_color'])
    plt.yticks([0, 5000, 10000, 15000, 20000], fontsize=8)
    plt.xticks(y, nations, fontsize=8, rotation=45)

    ticK_color = color_pallete['bg_color_sub2']
    ax.spines['bottom'].set_color(color_pallete['bg_color_sub1'])
    ax.spines['left'].set_color(color_pallete['bg_color_sub1'])
    ax.tick_params(axis='y', colors=ticK_color)  # 쪼매난 삐쭉 튀어난 애들
    ax.tick_params(axis='x', colors=ticK_color)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.xaxis.label.set_color(color_pallete['sub_color'])
    ax.yaxis.label.set_color(color_pallete['sub_color'])

    canvas = FigureCanvas(fig)
    canvas.draw()
    return canvas


# GDP 상관계수 3_2 (완료)
def setGraph3_2(color_pallete):
    feature = ['Gold', 'event_count', 'GDP']
    corr_feture = dataset1.corr()
    # 글자 색 DEFAULT
    matplotlib.rcParams['text.color'] = color_pallete['text_color']
    fig = plt.figure(figsize=(10, 10))
    # 배경색바꾸기
    fig.set_facecolor(color_pallete['bg_color'])
    # plt.title('GDP Corr Analysis', fontsize=15, color=color_pallete['text_color'])
    n_feature = len(feature)
    for i in range(n_feature):
        for j in range(n_feature):
            ax = fig.add_subplot(n_feature, n_feature, i * n_feature + j + 1)

            # 안에 있는 subplot 배경색 바꾸기
            ax.set_facecolor(color_pallete['bg_color_sub1'])
            # 산점도 컬러 추가
            plt.scatter(feature[j], feature[i], data=dataset1, s=1,
                        color=color_pallete['main_color'],
                        )
            # 축없애기
            remove_spines(plt)
            # x,y축 텍스트 변경
            ax.xaxis.label.set_color(color_pallete['bg_color_sub2'])
            ax.yaxis.label.set_color(color_pallete['bg_color_sub2'])

            if i == n_feature - 1:
                plt.xlabel(feature[j], fontsize=12)
            if j == 0:
                plt.ylabel(feature[i], fontsize=12)
            ax.annotate(np.round(corr_feture.loc[feature[i], feature[j]], 3), xy=(1, 0),
                        xycoords='axes fraction', fontsize=10,
                        horizontalalignment='right', verticalalignment='bottom')
    canvas = FigureCanvas(fig)
    canvas.draw()
    return canvas


def set_ax_color(axes, color_pallete):
    axes.set_facecolor(color_pallete['bg_color'])
    axes.xaxis.label.set_color(color_pallete['text_color'])
    axes.yaxis.label.set_color(color_pallete['text_color'])


def remove_spines(plt):
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['left'].set_visible(False)
    plt.gca().spines['bottom'].set_visible(False)
    plt.xticks(ticks=[])
    plt.yticks(ticks=[])
    return plt
