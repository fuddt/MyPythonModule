"""
ビルダーパターンの実用シナリオの例
1. ピザのオーダービルドシステム
ピザの注文システムはビルダーパターンを適用する典型的な例です。
ピザは様々なトッピング、クラストタイプ、サイズなど、複数の選択肢でカスタマイズされます。
ビルダーパターンを用いることで、異なるオプションを段階的に追加し、最終的な製品を組み立てるプロセスを簡単に管理できます。

2. コンピュータのカスタム組み立て
カスタムPCを組み立てる場合も、ビルダーパターンが有効です。
ユーザーはプロセッサ、RAM、ストレージデバイス、グラフィックスカードなど、
異なるハードウェアコンポーネントから選択して、自分のニーズに合わせたPCを構築します。ビルダーパターンによって、各ステップで正しい順序と構成が保証され、エラーの可能性を減少させます。

3. HTMLドキュメントジェネレーター
HTMLドキュメントを生成するシステムでは、異なるタグ（タイトル、ヘッダー、パラグラフなど）を組み合わせて全体のページを構築します。
ビルダーパターンを使用することで、複雑な文書も段階的に確実に構築できます。

実用的なサンプルコード（Python）
ピザのオーダービルドシステム
以下は、ピザの注文をカスタマイズするシンプルなビルダーパターンの実装例です。


"""

class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()
    
    def set_dough(self, dough):
        self.pizza.dough = dough
        return self
    
    def set_sauce(self, sauce):
        self.pizza.sauce = sauce
        return self
    
    def set_topping(self, topping):
        self.pizza.topping = topping
        return self
    
    def build(self):
        return self.pizza

class Pizza:
    def __init__(self):
        self.dough = None
        self.sauce = None
        self.topping = None
    
    def __str__(self):
        return f'Dough: {self.dough}, Sauce: {self.sauce}, Topping: {self.topping}'

# クライアントコード
def main():
    builder = PizzaBuilder()
    pizza = (builder.set_dough("thick")
                    .set_sauce("tomato")
                    .set_topping("mozzarella cheese")
                    .build())
    print(pizza)

if __name__ == "__main__":
    main()
