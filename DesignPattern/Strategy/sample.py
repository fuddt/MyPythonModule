from abc import ABC, abstractmethod

class Strategy(ABC):
    """アルゴリズムの共通インターフェース"""
    @abstractmethod
    def execute(self, data):
        pass

class ConcreteStrategyA(Strategy):
    """具体的なアルゴリズムA"""
    def execute(self, data):
        return sorted(data)

class ConcreteStrategyB(Strategy):
    """具体的なアルゴリズムB"""
    def execute(self, data):
        return reversed(sorted(data))

class Context:
    """アルゴリズムを使用するクライアントのクラス"""
    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    def set_strategy(self, strategy: Strategy):
        self._strategy = strategy

    def execute_strategy(self, data):
        return self._strategy.execute(data)

# 使用例
data = [23, 12, 78, 34, 56]
context = Context(ConcreteStrategyA())
result = context.execute_strategy(data)
print(list(result))

context.set_strategy(ConcreteStrategyB())
result = context.execute_strategy(data)
print(list(result))


