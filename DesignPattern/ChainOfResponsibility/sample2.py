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
