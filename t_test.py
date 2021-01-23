# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
import scipy.stats as st

# CSVの読み込み
# ここを書き換えることでデータを指定できる
df = pd.read_csv("Data/temperature.csv")

# 検定をする2列のHeaderを指定
xs = df["Osaka"]
ys = df["Tokyo"]

# 統計量tとp値の取得
# equal_var=Falseにするとwelchのt検定になります
t, p = st.ttest_ind(xs,ys,equal_var=False)

# 自由度
dfn     = len(xs)+len(ys)-2
# 平均値
loc = abs(xs.mean()-ys.mean())
# 標準偏差
# t = (X - Y) / u
scale =  loc / t
# 信頼区間
CI = st.t.interval( alpha=0.95, loc=loc, scale=scale, df=dfn)

print(f'p値: {p:.5f}')
print(f'信頼区間: ({CI[0]:.3f},{CI[1]:.3f})')