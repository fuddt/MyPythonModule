class RealSubject:
    """リモートで実行されるオブジェクトのクラス"""
    def request(self):
        print("RealSubject: Handling request.")

class Proxy:
    """RealSubjectの機能を制御するプロキシクラス"""
    def __init__(self, real_subject):
        self._real_subject = real_subject

    def request(self):
        if self.check_access():
            self._real_subject.request()
            self.log_access()
        else:
            print("Proxy: Access denied.")

    def check_access(self):
        # アクセス制御のロジック
        print("Proxy: Checking access prior to firing a real request.")
        return True

    def log_access(self):
        print("Proxy: Logging the time of request.")

# クライアントコード
real_subject = RealSubject()
proxy = Proxy(real_subject)
proxy.request()
