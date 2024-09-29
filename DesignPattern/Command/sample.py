from abc import ABC, abstractmethod

class Command(ABC):
    """
    抽象クラス：コマンドを表す

    メソッド：
        execute(): コマンドを実行する
        undo(): コマンドを元に戻す
    """

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class TextEditor:
    """
    テキストエディタを表すクラス
    """

    def __init__(self):
        self.content = ""  # テキスト内容

    def write(self, text):
        """
        テキストを追加する
        """
        self.content += text

    def delete_last(self, length):
        """
        最後のlength文字を削除する
        """
        self.content = self.content[:-length]

    def read(self):
        """
        現在のテキスト内容を取得する
        """
        return self.content


class WriteCommand(Command):
    """
    "書き込み" コマンドを表すクラス
    """

    def __init__(self, editor, text):
        self.editor = editor  # テキストエディタ
        self.text = text  # 書き込むテキスト

    def execute(self):
        """
        テキストを書き込む
        """
        self.editor.write(self.text)

    def undo(self):
        """
        書き込みを元に戻す
        """
        self.editor.delete_last(len(self.text))


class EditorHistory:
    """
    エディタ操作履歴を管理するクラス
    """

    def __init__(self):
        self.commands = []  # 実行したコマンドのリスト

    def execute_command(self, command):
        """
        コマンドを実行し、履歴に追加する
        """
        command.execute()
        self.commands.append(command)

    def undo(self):
        """
        最後の操作を元に戻す
        """
        if self.commands:
            command = self.commands.pop()
            command.undo()


# 使用例
editor = TextEditor()
history = EditorHistory()

# "Hello" を書き込むコマンドを実行
history.execute_command(WriteCommand(editor, "Hello"))

# "World" を書き込むコマンドを実行
history.execute_command(WriteCommand(editor, " World"))

# テキスト内容を出力
print(editor.read())  # 出力: Hello World

# 最後の操作を元に戻す
history.undo()

# テキスト内容を出力
print(editor.read())  # 出力: Hello

# もう一度元に戻す
history.undo()

# テキスト内容を出力
print(editor.read())  # 出力: （空文字列）