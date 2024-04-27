"""
このLoggerクラスはアプリケーション全体でのログ出力を管理し、ログレベルやメッセージの形式を統一します。
これにより、異なる部分からのログが一元的に扱われ、デバッグや運用の追跡が容易になります。

これらのコードはどちらもシングルトンパターンを利用しており、一度のインスタンス生成を保証し、
全体のリソース利用の効率を高めるとともに、設計の一貫性を保っています。
"""

class Logger:
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        if self._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            self._instance = self
            self.initialize_logger()

    def initialize_logger(self):
        # ログの設定を初期化
        import logging
        self.logger = logging.getLogger("ApplicationLogger")
        self.logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def log(self, level, message):
        if level.lower() == "info":
            self.logger.info(message)
        elif level.lower() == "error":
            self.logger.error(message)
        else:
            self.logger.debug(message)
