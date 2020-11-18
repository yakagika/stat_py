d
# 授業用にグラフの出力をまとめたModule

import pandas               as pd
import matplotlib.pyplot    as plt
import numpy                as np
import collections
import math

"""
header1 header2 header3 ...
value1  value2  value3  ...
の形のcsvから棒グラフを作成する
"""

def plotCSV2Bar(data_path = "", title="bar graph", y_label = "y_label"):
    df = pd.read_csv(data_path)
    print(df)
    labels = list(df.columns)
    values = list(df.iloc[0])
    y_position = np.arange(len(labels))
    plt.bar(y_position, values)
    plt.xticks(y_position,labels)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()


"""
header1 header2 header3 ...
value1  value2  value3  ...
の形のcsvから円グラフを作成する
"""

def plotCSV2Pie(data_path = "", title="pie graph"):
    df = pd.read_csv(data_path)
    print(df)
    labels = list(df.columns)
    values = list(df.iloc[0])
    plt.pie(values, labels=labels, autopct='%1.1f%%')
    plt.title(title)
    plt.show()

"""
xvalue header1   header2   header3 ...
xvalue y_value1  y_value2  y_value3  ...
xvalue y_value1  y_value2  y_value3  ...
xvalue y_value1  y_value2  y_value3  ...

の形のcsvから折れ線グラフを作成する
"""

def plotCSV2Plot(data_path = "", title="plot"):
    df = pd.read_csv(data_path)
    print(df)
    labels   = list(df.columns[1:])
    x_values = list(df[df.columns[0]])
    y_values = [list(df[x]) for x in labels]
    for i in range(len(labels)):
        plt.plot(x_values, y_values[i], label=labels[i])
    plt.title(title)
    plt.legend()
    plt.show()

"""
Header
Category
Category
Category
Category
Category
Category

の形のCSVからヒストグラムを作成する
data_type=0 ; カテゴリカルデータ
data_type=1 ; 量的データ
"""

def plotCSV2Hist(data_path="",title="Hist", data_type=0):
    # 関数名を sturgesNumber として引数をnとします
    def sturgesNumber(n):
        # 公式の通り k = 1 + log2 n
        # 階級数は整数が良いので,math.floor()で小数点以下を切り捨てます
        return (math.floor (1 + math.log2(n)))


    df = pd.read_csv(data_path)
    print(df)
    label  = df.columns[0]
    print(label)
    values = df[label]
    print(values)
    if data_type == 0 : #カテゴリカルデータ
        values.value_counts(sort=False).plot(kind="bar", width=1)
    else:
        plt.hist(values, bins=sturgesNumber(len(values)))

    plt.title(title)
    plt.show()


"""
Header Header
Value  Value
Value  Value
Value  Value

の形のcsvデータを読み込んで,散布図を作成します.
"""
def plotCSV2Scatter(data_path = "", title="Scatter"):
    df = pd.read_csv(data_path)
    print(df)
    x_value = list(df[df.columns[0]])
    y_value = list(df[df.columns[1]])
    plt.scatter(x_value, y_value)
    plt.title(title)
    plt.show()






