ビジターパターンは、オブジェクトの構造から処理を分離することを可能にする行動デザインパターンです。これにより、構造に変更を加えることなく、外部から新しい操作を構造の要素に追加できます。具体的には、ビジターと呼ばれる新しい操作を実装したクラスが、元のオブジェクト構造を「訪問」して処理を適用します。

使用シーン

ビジターパターンは以下のような場合に特に有用です：

オブジェクト構造に新しい操作を追加したいが、構造を構成するクラスを変更したくない場合：

構造が安定しており、頻繁に変更されないが、操作が頻繁に変更または追加される場合に適しています。

異なるクラスのオブジェクトに対して、異なる操作を実行したい場合：

オブジェクトの種類によって実行される処理が異なり、オブジェクトのクラスに多くの条件分岐を入れたくない時に役立ちます。

メリットとデメリット

メリット

拡張性：新しいビジターを作成することで、オブジェクトの構造に影響を与えることなく新しい操作を簡単に追加できます。

再利用性：同じオブジェクト構造に対して異なるビジターを適用することで、様々な処理を再利用することができます。

デメリット

ビジターの追加が困難な場合：オブジェクト構造が頻繁に変更される場合、ビジター自体もその変更に追従して更新する必要があります。

カプセル化の破壊：ビジターはオブジェクトの内部状態にアクセスするため、カプセル化の原則に反する可能性があります。

サンプルコード（Python）

以下は、複数の異なる要素クラスに対して異なる操作を適用するビジターパターンの実装例です。

```

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

```

このコード例では、Element クラス群が異なる種類の要素を表し、Visitor インターフェースが異なる操作を定義しています。具体的なビジター ConcreteVisitor1 は Visitor インターフェースを実装し、要素の種類に応じて異なる操作を実行します。各要素は accept メソッドを通じてビジターを受け入れ、ビジターに自身を渡すことで適切な操作が呼び出されます。

このパターンにより、各要素のクラスは単純化され、新しい操作を追加する際に要素のクラスを変更する必要がなくなります。代わりに新しいビジタークラスを追加することで、要素に新しい振る舞いを透過的に提供することが可能になります。

ビジターパターンをファイルシステムの要素に対する様々な操作を例に取り上げてみましょう。ここでは、ファイルとフォルダを訪問するビジターを使って、ファイルシステムの構造に対して異なるアクションを実行するシナリオを考えます。

シナリオ: ファイルシステムに対する操作

サンプルコード（Python）

```

from abc import ABC, abstractmethod

class FileSystemVisitor(ABC):
    """ファイルシステムの要素を訪問するビジターのインターフェース"""

    @abstractmethod
    def visit_file(self, file):
        pass

    @abstractmethod
    def visit_directory(self, directory):
        pass

class ConcreteFileSystemVisitor(FileSystemVisitor):
    """ファイルやディレクトリに対して特定の操作を行う具体的なビジター"""

    def visit_file(self, file):
        print(f"Accessing file: {file.name}")

    def visit_directory(self, directory):
        print(f"Accessing directory: {directory.name}")

class FileSystemElement(ABC):
    """ファイルシステムの要素のインターフェース"""

    @abstractmethod
    def accept(self, visitor):
        pass

class File(FileSystemElement):
    """ファイルを表すクラス"""

    def __init__(self, name):
        self.name = name

    def accept(self, visitor):
        visitor.visit_file(self)

class Directory(FileSystemElement):
    """ディレクトリを表すクラス"""

    def __init__(self, name):
        self.name = name
        self.elements = []

    def accept(self, visitor):
        visitor.visit_directory(self)
        for el in self.elements:
            el.accept(visitor)

    def add_element(self, element):
        self.elements.append(element)

# クライアントコード
root_directory = Directory("root")
file_a = File("file_a.txt")
file_b = File("file_b.csv")
sub_directory = Directory("subdir")

sub_directory.add_element(file_b)
root_directory.add_element(file_a)
root_directory.add_element(sub_directory)

visitor = ConcreteFileSystemVisitor()
root_directory.accept(visitor)

```

このシナリオでは、File と Directory クラスがファイルシステムの要素を表し、それぞれが FileSystemElement インターフェースを実装しています。ConcreteFileSystemVisitor クラスは FileSystemVisitor インターフェースを実装し、ファイルやディレクトリに対する特定の訪問処理を行います。

Directory クラスはコンポジットパターンのように、内部に複数の FileSystemElement を持つことができ、それらを一括で訪問できるようになっています。ビジターはディレクトリを訪問した後、そのディレクトリに含まれるすべての要素に対して再帰的に訪問処理を行います。

この例では、ビジターパターンを使用することでファイルシステムの要素に対する操作を柔軟に追加でき、それらの操作を要素のクラスから分離していることがわかります。将来的に新しい操作を追加する場合は、新しいビジタークラスを実装するだけで済みます。