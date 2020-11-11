# クラスの宣言
# Pokemonというものの種類を定義
class Pokemon():

    # コンストラクタの定義
    # ポケモンが生み出されたときにどんな特徴を定義すべきかを定義する
    # それぞれの特徴を属性という(ここでは,name,kind,levelの3つ)
    def __init__(self, name, kind, level):
        self.name       = name      # 引数の1つ目をnameに入れるよ
        self.kind       = kind      # 引数の2つ目をkindに入れるよ
        self.level      = level     # 引数の3つ目にlevelを入れるよ

    # メソッド= Pokemonという種類に属するモノが持つ機能
    # 1つ目の機能 強さをみる
    def view_strongness(self):
        print( "名前:"+ self.name
             + ", \nタイプ:"  + self.kind
             + ", \nレベル:"  + str(self.level))

# 具体的なポケモン(ポケモンクラスのインスタンス)=ピカチュウを作成
# 生み出すときに定義される特徴は,
# nama が ピカチュウ, タイプは電気, レベルは5
#pikachu = Pokemon("ピカチュウ","電気", 20)

# ピカチュウの強さを見てみる
#pikachu.view_strongness()

# Pokemonの派生クラスとして,電気ポケモンクラスを作成する
# 電気タイプのポケモンはポケモンの一種なのでポケモン全般の特徴も持つ
class Electric(Pokemon):

    # 電気タイプポケモンのコンストラクタ
    # タイプは電気なので予め定めておく
    def __init__(self,name,level):
        super().__init__(name,"電気",level)

    # 電気タイプだけが利用できるメソッド(電気技)
    def electro_ability(self,ability_number):
        if ability_number == 0:
            print("電気ショック! 威力:30")
        if ability_number == 1:
            print("10万ボルト! 威力:60" )
        else:
            print("カミナリ! 威力:120")

# Electricクラスのインスタンスとしてライチュウを生み出す
raichu = Electric("ライチュウ",30)

# ライチュウの強さを見てみる
raichu.view_strongness()

# ライチュウに電気技を使わせてみる
raichu.electro_ability(0)
raichu.electro_ability(1)
raichu.electro_ability(2)







