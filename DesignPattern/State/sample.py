from abc import ABC, abstractmethod

class DocumentState(ABC):
    """文書の状態を表す抽象基底クラス"""

    @abstractmethod
    def approve(self):
        pass

    @abstractmethod
    def deny(self):
        pass

class DraftState(DocumentState):
    """下書き状態を表すクラス"""
    
    def approve(self):
        return ModerationState()

    def deny(self):
        return RejectedState()

class ModerationState(DocumentState):
    """審査中状態を表すクラス"""
    
    def approve(self):
        return ApprovedState()

    def deny(self):
        return RejectedState()

class ApprovedState(DocumentState):
    """承認状態を表すクラス"""

    def approve(self):
        return self

    def deny(self):
        return self

class RejectedState(DocumentState):
    """却下状態を表すクラス"""

    def approve(self):
        return self

    def deny(self):
        return self

class Document:
    """文書を表すクラス"""
    
    def __init__(self):
        self.state = DraftState()

    def approve(self):
        self.state = self.state.approve()

    def deny(self):
        self.state = self.state.deny()

# クライアントコード
document = Document()
print(type(document.state))  # DraftState

document.approve()
print(type(document.state))  # ModerationState

document.approve()
print(type(document.state))  # ApprovedState

document.deny()  # 承認状態からは変わらない
print(type(document.state))  # ApprovedState
