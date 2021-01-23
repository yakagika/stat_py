# -*- coding:utf-8 -*-

import matplotlib.pyplot    as plt
import pandas               as pd
import random
import math


num_of_experiment = int(input("何回コインを投げるかを入力して下さい. \n"))

num_of_trial      = int(input("何回ベルヌーイ実験を繰り返すかを入力して下さい. \n"))

# ベルヌーイ試行をn回行った結果
# 表が出た回数のリストを返す
def bernoulli_trial(num_of_experiment, num_of_trial):
    front = 0
    res   = []
    for i in range(num_of_trial):
        for j in range(num_of_experiment):
            x = random.random()
            if x <= 0.5:
                front += 1
        res.append(front)
        front = 0
    return(res)

xs = bernoulli_trial(num_of_experiment, num_of_trial)

# データの分散
# 表が出る回数が平均値からどの程度乖離しているか
def variance(xs):
    total   = 0
    for x in xs:
        total += x
    ave = total / len(xs)
    deviation_total = 0
    for x in xs:
        deviation_total += (x - ave)**2

    return(deviation_total/len(xs))

# 2項分布の分散
# 表が出る回数が平均値からどの程度乖離しているか
def v(n,p):
    return(n*p*(1-p))

print("確率分布の標準偏差 np(1-p):", v(num_of_experiment,0.5)**(1/2))
print("実測値の標準偏差 1/n sum (x - bar x) ^2:", variance(xs)**(1/2))


# 実験結果の表示
df = pd.DataFrame([[x] for x in xs]).value_counts(sort=False)
x_values  = [x[0] for x in df.index]
y_values  = [y  for y in list(df)]
plt.bar(x_values,y_values)
plt.title("Distribution of the number of front side appears")
plt.xlabel("Number of fornt side appears")
plt.ylabel("Number of experiment")
plt.show()

# 確率分布の表示
l = len(xs)
y_values  = [(y / l) for y in list(df)]
plt.bar(x_values,y_values)
plt.title("Distribution of the number of front side appears")
plt.xlabel("Number of fornt side appears")
plt.ylabel("probability")
plt.show()


