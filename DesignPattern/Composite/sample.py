from abc import ABC, abstractmethod

class MenuComponent(ABC):
    """メニューコンポーネントの抽象基底クラス"""

    @abstractmethod
    def add(self, menu_component):
        raise NotImplementedError

    @abstractmethod
    def remove(self, menu_component):
        raise NotImplementedError

    @abstractmethod
    def get_name(self):
        raise NotImplementedError

    @abstractmethod
    def display(self):
        raise NotImplementedError

class MenuItem(MenuComponent):
    """単一のメニュー項目を表すクラス"""
    
    def __init__(self, name):
        self.name = name

    def add(self, menu_component):
        raise NotImplementedError("Leaf nodes can't add other components.")

    def remove(self, menu_component):
        raise NotImplementedError("Leaf nodes don't contain other components.")

    def get_name(self):
        return self.name

    def display(self):
        print(f"Item: {self.get_name()}")

class Menu(MenuComponent):
    """複合メニューコンポーネントを表すクラス"""
    
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, menu_component):
        self.children.append(menu_component)

    def remove(self, menu_component):
        self.children.remove(menu_component)

    def get_name(self):
        return self.name

    def display(self):
        print(f"Menu: {self.get_name()}")
        for component in self.children:
            component.display()

# クライアントコード
main_menu = Menu("Main Menu")
file_menu = Menu("File")
edit_menu = Menu("Edit")

new_file = MenuItem("New")
open_file = MenuItem("Open")
save_file = MenuItem("Save")
copy = MenuItem("Copy")
paste = MenuItem("Paste")

file_menu.add(new_file)
file_menu.add(open_file)
file_menu.add(save_file)

edit_menu.add(copy)
edit_menu.add(paste)

main_menu.add(file_menu)
main_menu.add(edit_menu)

main_menu.display()
