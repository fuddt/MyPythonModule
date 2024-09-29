class DataProvider:
    """データを提供するクラス"""
    def heavy_computation(self, data):
        print(f"Computing result for {data}...")
        return data * data  # 例としての計算

class CachingProxy:
    """DataProviderの結果をキャッシュするプロキシクラス"""
    def __init__(self, target):
        self._target = target
        self._cache = {}

    def heavy_computation(self, data):
        if data not in self._cache:
            self._cache[data] = self._target.heavy_computation(data)
        else:
            print("Returning cached result for:", data)
        return self._cache[data]

# クライアントコード
data_provider = DataProvider()
proxy = CachingProxy(data_provider)

print(proxy.heavy_computation(4))  # 最初の呼び出し、計算が行われる
print(proxy.heavy_computation(4))  # キャッシュから結果を取得
