from abc import ABC, abstractmethod

class VehicleBuilder(ABC):
    """車両ビルダーの抽象クラスです。すべてのビルダーはこのクラスを継承する必要があります。"""
    
    @abstractmethod
    def set_wheels(self, number_of_wheels):
        pass

    @abstractmethod
    def set_seats(self, number_of_seats):
        pass

    @abstractmethod
    def set_structure(self, structure_type):
        pass

    @abstractmethod
    def get_result(self):
        pass

class CarBuilder(VehicleBuilder):
    """車を構築する具体的なビルダークラスです。"""
    def __init__(self):
        self.vehicle = Vehicle()
    
    def set_wheels(self, number_of_wheels):
        self.vehicle.wheels = number_of_wheels
        return self
    
    def set_seats(self, number_of_seats):
        self.vehicle.seats = number_of_seats
        return self
    
    def set_structure(self, structure_type):
        self.vehicle.structure = structure_type
        return self
    
    def get_result(self):
        return self.vehicle

class Vehicle:
    """構築される車両のクラスです。"""
    def __init__(self):
        self.wheels = None
        self.seats = None
        self.structure = None
    
    def __str__(self):
        return f'Wheels: {self.wheels}, Seats: {self.seats}, Structure: {self.structure}'

class Director:
    """ビルダーオブジェクトを管理し、複数のビルダーを使用して異なるタイプの車両を構築します。"""
    def __init__(self):
        self._builder = None

    def construct(self, builder):
        self._builder = builder
        self._builder.set_wheels(4).set_seats(5).set_structure('Car')
        return self._builder.get_result()

# 使用例
director = Director()
car_builder = CarBuilder()
car = director.construct(car_builder)
print(car)
# >>> Wheels: 4, Seats: 5, Structure: Car