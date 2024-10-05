import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
from netmiko import ConnectHandler, NetmikoTimeoutException, NetmikoAuthenticationException
import pandas as pd
import time
from pathlib import Path
# CSVファイルからデバイス情報を読み込み
device_file = Path(__file__).parent / "./config.csv"

# ログファイルの設定
logging.basicConfig(filename='connection_test.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# デバイス情報の読み込み
devices = pd.read_csv(device_file)

# 接続を試みる関数
def test_connection(device):
    # Netmiko 用のデバイス定義
    cisco_device = {
        'device_type': 'cisco_ios',
        'host': device['host'],
        'port': device['port'],
        'username': device['username'],
        'password': device['password'],
    }
    # 接続のリトライ回数
    retries = 3
    for attempt in range(1, retries + 1):
        try:
            logging.info(f"Attempt {attempt}: Connecting to {device['host']} on port {device['port']}...")
            connection = ConnectHandler(**cisco_device)
            logging.info(f"Successfully connected to {device['host']}!")
            connection.disconnect()
            return f"Success: {device['host']}"
        except NetmikoTimeoutException:
            logging.error(f"Timeout occurred when connecting to {device['host']} on attempt {attempt}.")
        except NetmikoAuthenticationException:
            logging.error(f"Authentication failed for {device['host']} on attempt {attempt}.")
        time.sleep(2)  # リトライの前にちょっと待つ
    
    return f"Failed: {device['host']}"

# 複数のデバイスに対してマルチスレッドで接続
with ThreadPoolExecutor(max_workers=5) as executor:
    futures = [executor.submit(test_connection, device) for index, device in devices.iterrows()]
    
    for future in as_completed(futures):
        result = future.result()
        print(result)
        logging.info(result)