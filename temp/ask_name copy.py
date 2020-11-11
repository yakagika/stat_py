#-＊- coding:utf-8 -＊-

# もし条件Aなら,AAをする.
# もし,条件Bなら,BBをする.
# どれでもないならCCをする.
if 条件A:
    AA
elif 条件B:
    BB
else:
    CC

#xsの中身xを順番に取り出してyyyする
for x in xs:
    yyy

#例 : [0,1,2,3,4,5]の中身xを順番に取り出してprint(x)する
for x in [0,1,2,3,4,5]:
    print(x)



# ペットの種類を受け取ります.
kind = input("動物の名前をカタカナで入力してください. \n")

if      kind == "イヌ":
    print("ワンワン")

elif    kind == "ネコ":
    print("ニャンニャン")

else:
    print("???")


