"""
このConfigクラスはアプリケーションの設定情報を保持し、どこからでも容易にアクセスできます。
初回アクセス時にのみインスタンスが生成され、設定はメモリ内にロードされます。
"""



class Config:
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
            self.load_config()

    def load_config(self):
        # ここで設定ファイルから設定を読み込むか、デフォルト値を設定
        self.config = {
            "database_url": "localhost",
            "max_connections": 10,
            "log_level": "info",
        }

    def get_config(self, key):
        return self.config.get(key, None)
