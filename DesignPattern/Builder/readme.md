ビルダーパターンとは？
ビルダーパターンは、オブジェクトの生成過程をステップバイステップで行うことができるデザインパターンです。複雑なオブジェクトの構築を一連の部分的な構築手順に分解し、最終的なタイプの決定をサブクラスに委ねることができます。このパターンは、「ディレクター」と「ビルダー」の2つの異なるコンポーネントによって構成されます。

ビルダーパターンの使用シーン
複数のコンポーネントやオプションで構成されるオブジェクトを生成する場合
オブジェクトの生成プロセスが複数のステップに分かれており、それぞれのステップが複雑なロジックを含む場合
同じ作成プロセスで異なる表現や構成を持つオブジェクトを生成したい場合
メリット
構築プロセスの詳細なカプセル化: オブジェクトの実際の構築方法をクライアントから隠すことができます。
製品のバリエーションを容易にする: 異なるビルダーを使用することで、異なる属性や特徴を持つオブジェクトを同じ構築プロセスで作成できます。
オブジェクトの構築と表現の分離: ビルダーは最終オブジェクトの表現と構築プロセスを分離するため、同じ構築プロセスで異なる表現が得られます。
デメリット
設計が複雑になる: 小規模なオブジェクトの場合、ビルダーパターンを導入すると逆に設計が複雑になる可能性があります。
コードの量が増加する: ビルダーとディレクターのクラスを追加する必要があるため、コード量が増えます。
サンプルコード（Python）
以下は、Pythonでのビルダーパターンのサンプル実装です。ここでは、異なるタイプの車両を構築する例を示しています。

```
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

```
この例では、VehicleBuilder 抽象クラスを定義し、それを継承した CarBuilder クラスで具体的な車両の構築手順を定義しています。Director クラスは、構築プロセスを統括し、必要に応じて異なるビルダーを使い分けることができます。このようにビルダーパターンを使うことで、複雑なオブジェクトの構築を柔軟に制御できます。