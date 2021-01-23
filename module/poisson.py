# -*- coding:utf-8 -*-

import math
from scipy.special import comb

def bernoulli(n,x,p):
    return(comb(n,x) * (p ** x) * ((1-p) ** (n-x)))

def poisson(n,x,p):
    lamb = n * p
    return((math.e ** (-lamb)) * (lamb ** x) / math.factorial(x))
