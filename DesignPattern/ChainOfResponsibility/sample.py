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



print("Hello, World!")


