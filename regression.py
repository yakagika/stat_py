#-＊- coding:utf-8 -＊-

# データを読み込むためのパッケージ
import  pandas              as pd
# 相関係数を求めるためのパッケージ
import  numpy               as np

# CSVファイルを読み込んでデータフレームに格納
# Dataフォルダを作成し,そこにデータを入れておきましょう
df = pd.read_csv('Data/multiTimeline.csv')

# データの表示
print(df)

#分析するデータの選択
#xとyのHeader名を書き換えよう
x = df["AI"]
y = df["Python"]

# numpyで相関係数を求める
# 返り値が  [[xとxの相関係数=1, xとyの相関係数]
#           ,[yとxの相関係数,   yとyの相関係数=1]]
# なので, xとyの相関係数を取り出す
coef = np.corrcoef(x,y)[0][1]
print("相関係数:", coef)
