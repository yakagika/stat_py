import scipy.stats
import matplotlib.pyplot as plt

#実験回数を入力します
num = int(input("何回実験を行うかを半角英数字で入力しましょう \n"))

front = 0
back  = 0
process = []

for i in range(num):
    # ベルヌーイ分布に従う結果を返します
    result = scipy.stats.bernoulli.rvs(0.6)
    # 表が出た回数と,裏が出た回数を記録します.
    if result == 0:
        front += 1
    else:
        back  += 1
    process.append(front / (front + back))

# 結果を表示します
plt.plot(list(range(num)), process)
plt.title("The probability of getting a front.")
plt.show()

print("表が出る確率は", process[-1])