# -*- coding:utf-8 -*-

# 2進対数を返す math.log2() 関数などを利用するために必要なモジュール
import math

# 関数名を sturgesNumber として引数をnとします
def sturgesNumber(n):
    # 公式の通り k = 1 + log2 n
    # 階級数は整数が良いので,math.floor()で小数点以下を切り捨てます
    return (math.floor (1 + math.log2(n)))
