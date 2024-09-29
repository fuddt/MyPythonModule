class Memento:
    """エディタの状態を保存するためのメメントクラス"""
    
    def __init__(self, state):
        self._state = state

    def get_saved_state(self):
        return self._state

class Editor:
    """テキストを編集するエディタのクラス"""

    def __init__(self):
        self._content = ""

    def set_content(self, content):
        self._content = content

    def save(self):
        return Memento(self._content)

    def restore(self, memento):
        self._content = memento.get_saved_state()

    def __str__(self):
        return self._content

# クライアントコード
editor = Editor()

# テキストを設定し、状態を保存
editor.set_content("State1")
saved_state = editor.save()

# 状態を変更
editor.set_content("State2")

# 元の状態に戻す
editor.restore(saved_state)
print(editor)  # "State1" が出力される
