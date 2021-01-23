#-＊- coding:utf-8 -＊-
# プログラムに関する説明は今後別途行います.
# 今回は理解する必要はありません

# データを読み込むためのパッケージ
import  pandas              as pd
# 図示のためのパッケージ
import  matplotlib.pyplot   as plt
# 回帰分析を行うためのパッケージ
from    sklearn             import linear_model
# ヒートマップを作成するためのパッケージ
import seaborn as sns

# CSVファイルを読み込んでデータフレームに格納
# Dataフォルダを作成し,そこにデータを入れておきましょう
df = pd.read_csv('Data/multiple_regression_test.csv')

# データの表示
print(df)

# データの年度部分を抽出
year        = df["year"]
death       = df["death"]
index       = df["index"]
hospital    = df["hospital"]

#データをグラフで表示
plt.title('Data Visualization')
plt.ylabel('Year')
p1 = plt.plot(year, death)
p2 = plt.plot(year, index)
p3 = plt.plot(year, hospital)
plt.legend((p1[0],p2[0],p3[0]), ("Number of Death", "Economic Indicators", "Number of Hospitals"))
plt.show()

#散布図行列を作成してみる
pd.plotting.scatter_matrix(df.drop(['year'],axis=1), figsize=(15,15), range_padding=0.2)
plt.show()

# 多重共線性
# 相関のある要素はあまり利用しないほうが良い
sns.heatmap(df.drop(['year'], axis = 1).corr())
plt.show()


#予測モデルを作成(重回帰)
x = df.drop(['year','death'], axis = 1)
clf = linear_model.LinearRegression()
clf.fit(x,death)

#回帰係数と切片の抽出
a = clf.coef_
b = clf.intercept_

# 回帰係数
print("回帰係数:", a) # 回帰係数
print("切片:", b)     # 切片
print("決定係数:", clf.score(x, death)) # 決定係数

labels = ['Economic Indicators','Number of Hospitals']
plt.bar(labels,a)
plt.title('Number of Suicide')
plt.show()

# t検定
# t値が2以上なら支持, 1以下なら支持されない
# したほうが良いけど今回はしない





