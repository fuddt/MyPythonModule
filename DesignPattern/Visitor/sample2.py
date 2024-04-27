from abc import ABC, abstractmethod

class Visitor(ABC):
    """ビジターのインターフェイスを定義する抽象基底クラス"""

    @abstractmethod
    def visit_element_a(self, element):
        pass

    @abstractmethod
    def visit_element_b(self, element):
        pass

class ConcreteVisitor1(Visitor):
    """具体的なビジター1"""

    def visit_element_a(self, element):
        print(f"{element.operation_a()} visited by ConcreteVisitor1")

    def visit_element_b(self, element):
        print(f"{element.operation_b()} visited by ConcreteVisitor1")

class Element(ABC):
    """要素のインターフェイスを定義する抽象基底クラス"""

    @abstractmethod
    def accept(self, visitor):
        pass

class ElementA(Element):
    """要素A"""

    def operation_a(self):
        return "ElementA"

    def accept(self, visitor):
        visitor.visit_element_a(self)

class ElementB(Element):
    """要素B"""

    def operation_b(self):
        return "ElementB"

    def accept(self, visitor):
        visitor.visit_element_b(self)

# クライアントコード
elements = [ElementA(), ElementB()]
visitor1 = ConcreteVisitor1()

for element in elements:
    element.accept(visitor1)
