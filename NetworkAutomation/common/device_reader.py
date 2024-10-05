import pandas as pd
class DeviceReader:
    def __init__(self, device_file):
        self.device_file = device_file
        self.devices = None
        
    def read_devices(self) -> None:
        # pandasを使ってCSVファイルを読み込む
        self.devices = pd.read_csv(self.device_file)
    
    def show_devices(self) -> None:
        if self.devices is None:
            print("デバイス情報が読み込まれていません。")
            return
        
        print(self.devices)
    
    def get_devices(self, host: str, device_type: str) -> dict | None:
        if self.devices is None:
            print("デバイス情報が読み込まれていません。")
            return
        data = self.devices[self.devices['host'] == host].to_dict(orient='records')[0]
        # デバイスタイプを追加する
        data['device_type'] = device_type
        return data
    
        