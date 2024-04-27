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
