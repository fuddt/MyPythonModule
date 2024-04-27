テンプレートメソッドパターン（Template Method Pattern）

テンプレートメソッドパターンは、ある処理の骨組み（テンプレート）をスーパークラスで定義し、その具体的な内容をサブクラスで個別に定義するための行動デザインパターンです。このパターンは、アルゴリズムの構造を一つのメソッドにカプセル化し、その一部をサブクラスで実装できるようにすることで、アルゴリズムの再定義なしに特定のステップを変更することができます。

使用シーン

テンプレートメソッドパターンは以下のような場合に特に有用です：

複数のアルゴリズムやクラスが類似の手順を持っているが、いくつかのステップが異なる場合：

同じ基本アルゴリズムに対して、特定のステップだけをカスタマイズしたいときに適しています。

リファクタリング時に共通の動作をスーパークラスに抽出したい場合：

コードの重複を減らし、サブクラスのオーバーライドのみを通じて特定の振る舞いを定義したいときに役立ちます。

メリットとデメリット

メリット

コードの重複を減らす：共通のアルゴリズムをスーパークラスに一度実装することで、重複を減らすことができます。

拡張性：新しいサブクラスを作成することで、簡単に新しい振る舞いを追加できます。

デメリット

サブクラスによる設計の制約：スーパークラスのテンプレートメソッドが厳密であるため、サブクラスがそれに従う必要があります。

複雑なアルゴリズムの隠蔽：アルゴリズムの一部のみがサブクラスで可視化されるため、アルゴリズムの全体像を理解しにくくなる場合があります。

サンプルコード（Python）

以下は、ゲームのフレームワークにテンプレートメソッドパターンを適用した例です。

```

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
chess.play() # playを呼び出せば決まった順序で実行される

soccer = Soccer()
soccer.play() # playを呼び出せば決まった順序で実行される

```

この例では、Game がスーパークラスで、ゲームの全体的な流れを定義するテンプレートメソッド play() を持っています。具体的なゲームの種類ごとに Chess や Soccer のようなサブクラスがあり、それぞれが setup、start_play、end_play のメソッドをオーバーライドして独自の実装を提供します。これにより、ゲームの基本的な骨組みを変更することなく、新しいゲームを簡単に追加できるようになります。

