class ExpensiveObject:
    """ロードに多大なコストがかかるオブジェクトのクラス"""
    def __init__(self):
        print("Loading a heavy object...")
        # 何らかの重い処理を想定

    def operation(self):
        print("Performing an operation on the object...")

class LazyProxy:
    """ExpensiveObjectの遅延初期化を行うプロキシクラス"""
    def __init__(self):
        self._expensive_object = None

    def operation(self):
        if not self._expensive_object:
            self._expensive_object = ExpensiveObject()  # 実際に必要になった時にインスタンス化
        self._expensive_object.operation()

# クライアントコード
proxy = LazyProxy()
proxy.operation()  # この時点で初めてExpensiveObjectがロードされる
