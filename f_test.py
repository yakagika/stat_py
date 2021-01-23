#-＊- coding:utf-8 -＊-

import  pandas  as pd
import  numpy   as np
from    scipy   import stats


# データの読み込み
# ファイル名を変えれば違うデータが読み込める
df = pd.read_csv("Data/temperature.csv")

# 読み込む列の指定
x = df["Tokyo"]
y = df["Osaka"]

# それぞれの不偏分散
x_var = np.var(x, ddof=1)
y_var = np.var(y, ddof=1)

# それぞれの自由度
x_df = len(x) - 1
y_df = len(y) - 1

# フィッシャーのF検定量
F = x_var / y_var

# 左側累積確率
left_pval = stats.f.cdf(F, x_df, y_df)

# 右側累積確率
right_pval = stats.f.sf(F, x_df, y_df)

# 両側確率
# 𝐹_(1−𝛼\/2) (𝑚−1,𝑛−1)≤𝐹≤𝐹_(𝛼\/2) (𝑚−1,𝑛−1)
# なので,片方が0.025 以下ならOUT
both = min(left_pval, right_pval)

print('p-value: ', round(both,5))
if both < 0.25 :
    print('帰無仮説: x_var == y-var は棄却される')
else:
    print('帰無仮説: x_var == y-var は棄却されない')


