# -*- coding:utf-8 -*-
import pandas as pd 

# データの作成
df = pd.DataFrame([['Data A', 'cat',  60, 22],
                   ['Data B', 'dog',  55, 34],
                   ['Data C', 'dog',  82, 54],
                   ['Data D', 'bird', 43, 17]],
                   columns=['Person', 'pet', 'weight', 'age'])
print(df)

# データの書き出し
df.to_csv('Data/make_data.csv')
