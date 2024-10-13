import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('medical_examination.csv')

df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2)).apply(lambda x: 1 if x > 25 else 0)

df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)

def draw_cat_plot():
    cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    
    plot_cat = cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    
    img = sns.catplot(x="variable", y="total", hue="value", col="cardio", data=cat, kind="bar", height=5, aspect=1).fig
    
    return img

def draw_heat_map():
    calor = df[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))]
    correlacao = calor.corr()
    mascara = np.triu(np.ones_like(correlacao, dtype=bool))
    
    fig, ax = plt.subplots(figsize=(12, 12))
    sns.heatmap(correlacao, mask=mascara, annot=True, fmt='.1f', square=True, center=0, cmap='coolwarm', ax=ax)

    return fig
