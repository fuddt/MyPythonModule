from abc import ABC, abstractmethod

class Game(ABC):
    """ゲームフレームワークのための抽象基底クラスです。"""
    
    def play(self):
        """ゲームのテンプレートメソッドです。"""
        self.setup()
        self.start_play()
        self.end_play()

    @abstractmethod
    def setup(self):
        """ゲーム開始前の準備を行います。サブクラスで具体的な実装が必要です。"""
        pass

    @abstractmethod
    def start_play(self):
        """ゲームのプレイを開始します。サブクラスで具体的な実装が必要です。"""
        pass

    @abstractmethod
    def end_play(self):
        """ゲームの後処理を行います。サブクラスで具体的な実装が必要です。"""
        pass

class Chess(Game):
    """チェスゲームのためのクラスです。"""
    
    def setup(self):
        print("Setting up a chess board.")

    def start_play(self):
        print("Starting a game of chess.")

    def end_play(self):
        print("Ending the chess game.")

class Soccer(Game):
    """サッカーゲームのためのクラスです。"""
    
    def setup(self):
        print("Setting up a soccer match.")

    def start_play(self):
        print("Starting the soccer match.")

    def end_play(self):
        print("Ending the soccer match.")

# クライアントコード
chess = Chess()
chess.play()

soccer = Soccer()
soccer.play()
