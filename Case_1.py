# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
url = 'https://raw.githubusercontent.com/DUanalytics/datasets/master/csv/denco.csv'

import pandas as pd
df = pd.read_csv(url)
df.describe()
df.shape
df.columns
df.head(3)
len(df)
df.dtypes
df['region'] = df['region'].astype('category')
df.dtypes

df.region.value_counts()
df.region.value_counts().plot(kind = 'bar')

df.custname.value_counts()
df.custname.value_counts().head(5)
df.custname.value_counts().tail(5)
df.groupby('custname').revenue.sum().sort_values(ascending=False)

df.groupby('partnum').revenue.sum().sort_values(ascending=False)
df.groupby('partnum').margin.sum().sort_values(ascending=False)
df.groupby('partnum').revenue.max().sort_values(ascending=False)
df.groupby('partnum').margin.max().sort_values(ascending=False)

df.groupby('partnum').size().sort_values(ascending=False)

df.groupby('region').revenue.sum().sort_values(ascending=True).plot(kind = 'barh')


