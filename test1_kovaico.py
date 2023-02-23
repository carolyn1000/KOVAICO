# -*- coding: utf-8 -*-
"""test1_KOVAICO.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17DqOWTGloJpFwsXROssSyFvLscmAd7Lf
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv('/content/prime - prime.csv.csv')

data.info()

data.shape

data.head()

data.tail()

data.isnull().sum()

data['director']=data['director'].fillna('unknown')

data.isnull().sum()

data=data.dropna(axis=0)

data

data['release_year'].min()

data['release_year'].max()

data['release_year'].mode()

data.isnull().sum()

data['type'].unique()

sns.countplot(data['type'])

#content control rating is seen using countplot
plt.figure(figsize=(10,10))
sns.countplot(data['rating'])

from wordcloud import WordCloud, STOPWORDS

comment_words = ','
stopwords = set(STOPWORDS)
 
for val in data.listed_in:
   val = str(val)
 
tokens = val.split()
for i in range(len(tokens)):
        tokens[i] = tokens[i].lower()
     
comment_words += " ".join(tokens)+" "
wordcloud = WordCloud(stopwords = stopwords,
                min_font_size = 10).generate(comment_words)                 
plt.figure(figsize = (8, 8))
plt.imshow(wordcloud)
plt.show()