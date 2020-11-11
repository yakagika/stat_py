#-＊- coding:utf-8 -＊-

import pandas as pd

# CSVファイルを読み込んでデータフレームに格納
# Dataフォルダを作成し,そこにデータを入れておきましょう
df = pd.read_csv('Data/salary_data.csv')

# データの表示
print(df)
