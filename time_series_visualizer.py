import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dados = pd.read_csv("/content/fcc-forum-pageviews.csv", parse_dates=["date"], index_col="date")
dados = dados[
    (dados['value'] >= dados['value'].quantile(0.025)) & 
    (dados['value'] <= dados['value'].quantile(0.975))
]

def draw_line_plot():
    img, ax = plt.subplots(figsize=(12, 6))

    ax.plot(dados.index, dados['value'], color='skyblue', linewidth=1)
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    return img

def draw_bar_plot():
    dados_bar = dados.copy()
    dados_bar['year'] = dados_bar.index.year
    dados_bar['month'] = dados_bar.index.month_name()
    dados_bar = dados_bar.groupby(['year', 'month'])['value'].mean().unstack()

    img = dados_bar.plot(kind='bar', figsize=(12, 6)).figure
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months')
    plt.xticks(rotation=45)
    return img

def draw_box_plot():
    dados_box = dados.copy()
    dados_box.reset_index(inplace=True)
    dados_box['year'] = dados_box['date'].dt.year
    dados_box['month'] = dados_box['date'].dt.strftime('%b')
    dados_box['month'] = pd.Categorical(dados_box['month'], 
                                     categories=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                                                 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], 
                                     ordered=True)
    img, axes = plt.subplots(1, 2, figsize=(18, 6))
    sns.boxplot(x='year', y='value', data=dados_box, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')
    sns.boxplot(x='month', y='value', data=dados_box, ax=axes[1])

    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')
    return img

draw_line_plot()
draw_bar_plot()
draw_box_plot()