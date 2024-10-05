from common.device_reader import DeviceReader

# デバイス情報の読み込み
device_reader = DeviceReader("common/config.csv")
device_reader.read_devices()

# デバイス情報の表示
device_reader.show_devices()

# 特定のデバイス情報の取得
device = device_reader.get_devices