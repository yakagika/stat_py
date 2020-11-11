# -*- coding:utf-8 -*-

# このファイルが有るところからみて 
# module フォルダの中の,basic_statistics.py を stat という名前で読み込みます.
import module.basic_statistics as stat 

print("算術平均:", stat.mean([1,2,3]))
print("幾何平均:", stat.geometric_mean([1,2,3]))
print("調和平均:", stat.harmonic_mean([1,2,3]))


