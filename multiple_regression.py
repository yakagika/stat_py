#-＊- coding:utf-8 -＊-

# データを読み込むためのパッケージ
import  pandas              as pd
# 図示のためのパッケージ
import  matplotlib.pyplot   as plt
# ヒートマップを作成するためのパッケージ
import seaborn as sns
# 回帰分析を行うためのパッケージ
import statsmodels.api as sm


# CSVファイルを読み込んでデータフレームに格納
# Dataフォルダを作成し,そこにデータを入れておきましょう
df = pd.read_csv('Data/wifi.csv')


# データの表示
print(df)

# 被説明変数のヘッダーを指定
Y_label = 'math'
# 正規化 min-max scaling
Y = (df[Y_label] - df[Y_label].min()) \
  / (df[Y_label].max() - df[Y_label].min())
print(Y)

# 説明変数のヘッダーを指定
X_labels = ['pc','board']
# 正規化 min-max scaling
X = (df[X_labels] - df[X_labels].min())  \
  / (df[X_labels].max() - df[X_labels].min())
print(X)

# 多重共線性のチェック
# 相関のある要素はあまり利用しないほうが良い
#散布図行列を作成してみる
pd.plotting.scatter_matrix(X, range_padding=0.2)
plt.show()

#ヒートマップで確認
sns.heatmap(X.corr())
plt.show()

#予測モデルを作成(重回帰)
X = sm.add_constant(X)
model = sm.OLS(Y,X)
result = model.fit()

#結果の表示
print(result.summary())

#回帰係数の図示
plt.bar(X_labels,result.params[1:])
plt.title('Regression coefficient')
plt.show()

