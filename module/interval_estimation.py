#-＊- coding:utf-8 -＊-
from scipy.stats import norm, t
import numpy as np
import pandas as pd


"""
Header名,Path,確率を渡すとt分布の信頼区間を返す関数
"""
def t_interval(path, header, percent=95):
    df   = pd.read_csv(path)
    data = df[header]
    print(data)
    size = len(data)
    dfn  = size - 1
    # 標本標準偏差
    s = np.std(data)
    print("標本標準偏差:", s)

    # 標本平均
    mean = np.mean(data)
    print("標本平均",mean)

    t_a  = t.ppf(df=dfn,q= (1 - (100 - percent) /200))
    lower = mean - t_a * (s / np.sqrt(size))
    upper = mean + t_a * (s / np.sqrt(size))
    return(lower, upper)

"""
Header名,Path名,母集団標準偏差,確率,を渡すと標準正規分布の信頼区間を返す関数
"""
def z_interval(path, header,std, percent=95):
    df   = pd.read_csv(path)
    data = df[header]
    print(data)
    size = len(data)
    dfn  = size - 1

    # 標本平均
    mean = np.mean(data)
    print("標本平均",mean)

    t_a  = norm.ppf(q= (1 - (100 - percent) /200))
    lower = mean - t_a * (std / np.sqrt(size))
    upper = mean + t_a * (std / np.sqrt(size))
    return(lower, upper)


