class CelsiusThermometer:
    """摂氏温度を提供するクラスです。"""
    def get_temperature(self):
        return 23.0  # 摂氏温度を返します。

class FahrenheitAdapter:
    """華氏温度へのアダプターです。CelsiusThermometerクラスをラップして、温度を華氏で返します。"""
    def __init__(self, celsius_thermometer):
        self._celsius_thermometer = celsius_thermometer
    
    def get_temperature(self):
        celsius = self._celsius_thermometer.get_temperature()
        return (celsius * 9 / 5) + 32

# クライアントコード
def client_code(thermometer):
    """サーモメーターのインターフェースを通じて温度を取得し、表示するクライアント関数です。"""
    print(f"Temperature: {thermometer.get_temperature()}°")

# 既存の摂氏温度計を使用
celsius_thermometer = CelsiusThermometer()
client_code(celsius_thermometer)

# 華氏で温度を取得するためにアダプターを使用
fahrenheit_thermometer = FahrenheitAdapter(celsius_thermometer)
client_code(fahrenheit_thermometer)
