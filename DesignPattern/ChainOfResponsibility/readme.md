チェーン・オブ・レスポンシビリティパターンは、複数のオブジェクトのチェーンを通じてリクエストを送ることにより、リクエストの送信者と受信者の間の結びつきを避ける行動デザインパターンです。リクエストを処理する責任を持つオブジェクトのチェーンがあり、リクエストはチェーン上で次々に渡されます。各ハンドラはリクエストを処理するか、それをチェーンの次のハンドラに渡すかを選択できます。

使用シーン

チェーン・オブ・レスポンシビリティパターンは以下のような場合に特に有用です：

複数のオブジェクトがリクエストを処理できるが、具体的にどのオブジェクトが処理するかは実行時にのみ決定される場合：

例えば、イベントハンドリングシステムやログ処理システムでよく見られます。

リクエストを処理するオブジェクトのセットを動的に指定したい場合：

実行時にリクエスト処理の責任を持つオブジェクトを変更できる必要があるときに役立ちます。

メリットとデメリット

メリット

低結合性：リクエストの送信者と受信者が疎結合であるため、システムの柔軟性と再利用性が向上します。

動的な責任の付与：実行時にチェーンの構造を変更することができます。

デメリット

リクエストの保証なし：リクエストが必ずしも処理されるわけではないため、チェーンのどの部分で処理されるか保証がありません。

デバッグの複雑性：リクエストが複数のハンドラを通過すると、デバッグが困難になることがあります。

サンプルコード（Python）

以下は、エラーログ処理を担当する異なるレベルのロガーを作成するためのチェーン・オブ・レスポンシビリティパターンの実装例です。

```

from abc import ABC, abstractmethod

class Handler(ABC):
    """ハンドラの抽象基底クラス"""
    
    @abstractmethod
    def set_next(self, handler):
        pass

    @abstractmethod
    def handle(self, request):
        pass

class AbstractHandler(Handler):
    """ハンドラのデフォルトの振る舞いを提供する抽象クラス"""

    _next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    def handle(self, request):
        if self._next_handler:
            return self._next_handler.handle(request)
        return None

class InfoHandler(AbstractHandler):
    """Infoレベルのエラーを処理するハンドラ"""

    def handle(self, request):
        if request == "info":
            return f"InfoHandler: Handling {request}"
        else:
            return super().handle(request)

class WarnHandler(AbstractHandler):
    """Warnレベルのエラーを処理するハンドラ"""

    def handle(self, request):
        if request == "warn":
            return f"WarnHandler: Handling {request}"
        else:
            return super().handle(request)

class ErrorHandler(AbstractHandler):
    """Errorレベルのエラーを処理するハンドラ"""

    def handle(self, request):
        if request == "error":
            return f"ErrorHandler: Handling {request}"
        else:
            return super().handle(request)

# クライアントコード
info_handler = InfoHandler()
warn_handler = WarnHandler()
error_handler = ErrorHandler()

info_handler.set_next(warn_handler).set_next(error_handler)

# クライアントからのリクエストは、チェーンを通じて適切なハンドラに渡されます。
print(info_handler.handle("info"))   # InfoHandler: Handling info
print(info_handler.handle("warn"))   # WarnHandler: Handling warn
print(info_handler.handle("error"))  # ErrorHandler: Handling error

```

このコード例では、Handler インターフェースとその抽象実装である AbstractHandler クラスが、ハンドラの共通の振る舞いを定義しています。具体的なハンドラ InfoHandler、WarnHandler、ErrorHandler は、それぞれ特定の種類のリクエストを処理します。リクエストは info から開始して、適切なハンドラが見つかるまでチェーンを通じて渡されます。各ハンドラはリクエストを処理するか、次のハンドラにリクエストを渡します。

別のシナリオとして、ヘルプデスクのサポートチケット処理システムにおけるチェーン・オブ・レスポンシビリティパターンの適用を見てみましょう。サポートチケットは技術的な難易度やカテゴリーに応じて異なるサポートレベルにルーティングされる必要があります。

シナリオ: ヘルプデスクのサポートチケット処理

サンプルコード（Python）

```

class SupportTicket:
    """サポートチケットを表すクラス"""
    def __init__(self, issue_type):
        self.issue_type = issue_type
        self.handled = False

class Handler(ABC):
    """リクエストを処理するハンドラの抽象基底クラス"""
    
    @abstractmethod
    def set_next(self, handler):
        pass

    @abstractmethod
    def handle(self, ticket):
        pass

class AbstractHandler(Handler):
    """ハンドラのデフォルトの振る舞いを提供する抽象クラス"""
    
    _next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    def handle(self, ticket):
        if self._next_handler:
            return self._next_handler.handle(ticket)
        return None

class BasicSupportHandler(AbstractHandler):
    """基本的な問題を処理するハンドラ"""

    def handle(self, ticket):
        if ticket.issue_type == "basic":
            ticket.handled = True
            print(f"BasicSupportHandler: Handled {ticket.issue_type}")
            return ticket
        else:
            return super().handle(ticket)

class AdvancedSupportHandler(AbstractHandler):
    """高度な問題を処理するハンドラ"""

    def handle(self, ticket):
        if ticket.issue_type == "advanced":
            ticket.handled = True
            print(f"AdvancedSupportHandler: Handled {ticket.issue_type}")
            return ticket
        else:
            return super().handle(ticket)

class ExpertSupportHandler(AbstractHandler):
    """専門的な問題を処理するハンドラ"""

    def handle(self, ticket):
        if ticket.issue_type == "expert":
            ticket.handled = True
            print(f"ExpertSupportHandler: Handled {ticket.issue_type}")
            return ticket
        else:
            return super().handle(ticket)

# クライアントコード
basic_handler = BasicSupportHandler()
advanced_handler = AdvancedSupportHandler()
expert_handler = ExpertSupportHandler()

basic_handler.set_next(advanced_handler).set_next(expert_handler)

# チケット発行と処理
ticket1 = SupportTicket("basic")
ticket2 = SupportTicket("advanced")
ticket3 = SupportTicket("expert")

basic_handler.handle(ticket1)  # BasicSupportHandler: Handled basic
basic_handler.handle(ticket2)  # AdvancedSupportHandler: Handled advanced
basic_handler.handle(ticket3)  # ExpertSupportHandler: Handled expert

```

このシナリオでは、複数レベルのサポートハンドラがあり、それぞれが特定の種類のサポートチケットを処理します。チケットは最初に基本サポートハンドラに渡され、問題の難易度に応じて適切なハンドラが処理するまでチェーンを通過します。もし基本ハンドラが問題を処理できなければ、次の高度な問題を扱うハンドラにチケットが移行し、最終的に専門家ハンドラまで行くことがあります。

このパターンにより、サポートチケットが適切なレベルのサポートスタッフによって効率的に処理されることを保証する柔軟で再利用可能なシステムを設計することができます。各ハンドラは自分の責任範囲のリクエストだけを処理し、それ以外のものはチェーンを通じて次のハンドラに渡すことができます。