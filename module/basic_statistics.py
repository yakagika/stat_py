# -*- coding:utf-8 -*-

# 算術平均
def mean(xs):
    return sum(xs) / len(xs)

def mean2(xs):
    return sum(map(lambda x: x/len(xs),xs))

# 幾何平均
def geometric_mean(xs):
    multiplicated = 1
    for x in xs:
        multiplicated = multiplicated * x
    return multiplicated ** (1/len(xs))

#調和平均
def harmonic_mean(xs):
    fractedSum = sum(map(lambda x:(1/x), xs))
    return len(xs) / fractedSum

def bunnboni(xs):
    result = 0
    for x in xs:
        result += 1/x
    return result

def harmonic_mean2(xs):
    return len(xs) / sum(bunnboni(xs))

# 中央値
def median(xs):
    xss = sorted(xs)
    length = len(xss)
    if length % 2 != 0:
        return xss[((length + 1) // 2) -1]
    else:
        return (xss[(length/2) - 1] + xss[(length/2)])/2

#最大値 普通の
def get_max1(xs):
    res = xs[0]
    for i in range(1, len(xs)):
        if xs[i] >= res:
            res = xs[i]
    return res


#最大値 再帰
def get_max2(xs):
    if len(xs) == 0:
        return 0
    elif len(xs) == 1:
        return xs[0]
    elif xs[0] >= get_max2(xs[1:]):
        return xs[0]
    else:
        return get_max2(xs[1:])

# 最大値 内包表記
def and_list(xs):
    res = xs[0]
    for x in xs:
        res = x and res
    return res

def get_max3(xs):
    return [x for x in xs if and_list([x >= y for y in xs])]





