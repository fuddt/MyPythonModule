from abc import ABC, abstractmethod

class Graphic(ABC):
    """グラフィックオブジェクトの共通インターフェース"""
    
    @abstractmethod
    def draw(self):
        pass

class CompositeGraphic(Graphic):
    """コンポジットクラス。他のグラフィックオブジェクトを子として持つことができる。"""
    
    def __init__(self):
        self.children = []
    
    def add(self, graphic):
        self.children.append(graphic)
    
    def remove(self, graphic):
        self.children.remove(graphic)
    
    def draw(self):
        for graphic in self.children:
            graphic.draw()

class Circle(Graphic):
    """単純な円を表現するクラス"""
    
    def draw(self):
        print("Circle drawn")

class Square(Graphic):
    """単純な四角形を表現するクラス"""
    
    def draw(self):
        print("Square drawn")

# クライアントコード
composite = CompositeGraphic()
composite.add(Circle())
composite.add(Square())

composite.draw()  # すべての子グラフィックオブジェクトを描画
