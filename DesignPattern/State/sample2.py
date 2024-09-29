from abc import ABC, abstractmethod

class TrafficLightState(ABC):
    """交通信号機の状態を表す抽象基底クラス"""

    @abstractmethod
    def change(self, traffic_light):
        pass

    @abstractmethod
    def display(self):
        pass

class RedLightState(TrafficLightState):
    """赤信号の状態を表すクラス"""
    
    def change(self, traffic_light):
        traffic_light.state = GreenLightState()

    def display(self):
        print("RED - Cars should stop")

class YellowLightState(TrafficLightState):
    """黄信号の状態を表すクラス"""
    
    def change(self, traffic_light):
        traffic_light.state = RedLightState()

    def display(self):
        print("YELLOW - Cars should prepare to stop")

class GreenLightState(TrafficLightState):
    """緑信号の状態を表すクラス"""
    
    def change(self, traffic_light):
        traffic_light.state = YellowLightState()

    def display(self):
        print("GREEN - Cars can go")

class TrafficLight:
    """交通信号機を表すクラス"""
    
    def __init__(self):
        self.state = RedLightState()

    def change(self):
        self.state.change(self)

    def display(self):
        self.state.display()

# クライアントコード
traffic_light = TrafficLight()
traffic_light.display()  # 初期状態: 赤信号

# 信号機の状態を変更して表示
traffic_light.change()
traffic_light.display()  # 緑信号

traffic_light.change()
traffic_light.display()  # 黄信号

traffic_light.change()
traffic_light.display()  # 赤信号
