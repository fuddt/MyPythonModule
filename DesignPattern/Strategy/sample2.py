from abc import ABC, abstractmethod
import statistics

class StatStrategy(ABC):
    """統計アルゴリズムのためのストラテジー基底クラス"""
    @abstractmethod
    def calculate(self, data):
        pass

class AverageStrategy(StatStrategy):
    """平均値を計算する具体的なストラテジー"""
    def calculate(self, data):
        return statistics.mean(data)

class MedianStrategy(StatStrategy):
    """中央値を計算する具体的なストラテジー"""
    def calculate(self, data):
        return statistics.median(data)

class ModeStrategy(StatStrategy):
    """最頻値を計算する具体的なストラテジー"""
    def calculate(self, data):
        return statistics.mode(data)

class Context:
    """ストラテジーの使用をコントロールするコンテキストクラス"""
    def __init__(self, strategy: StatStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: StatStrategy):
        self._strategy = strategy

    def execute_strategy(self, data):
        return self._strategy.calculate(data)

# 使用例
data = [1, 2, 2, 3, 4, 5, 5, 5, 6]

context = Context(AverageStrategy())
print("Average:", context.execute_strategy(data))

context.set_strategy(MedianStrategy())
print("Median:", context.execute_strategy(data))

context.set_strategy(ModeStrategy())
print("Mode:", context.execute_strategy(data))
