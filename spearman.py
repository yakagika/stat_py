#-＊- coding:utf-8 -＊-
# データを読み込むためのパッケージ
import  pandas              as pd
# 相関係数を求めるためのパッケージ
from scipy.stats import spearmanr

# CSVファイルを読み込んでデータフレームに格納
# Dataフォルダを作成し,そこにデータを入れておきましょう

df = pd.read_csv('Data/spearman.csv')

# データの表示
print(df)

#分析するデータの選択
#xとyのHeader名を書き換えよう
x = df["FIFA"]
y = df["WBSC"]

# sciypyで相関係数を求める
correlation, pvalue = spearmanr(x, y)
print("相関係数:",correlation)