from napalm import get_network_driver

# ドライバの取得（Cisco IOSを対象）
driver = get_network_driver('ios')

# デバイス情報
cisco_device = {
    'hostname': '10.10.****',
    'username': 'developer',
    'password': '*****',
    'optional_args': {'port': 22}
}

# ドライバのインスタンスを作成
device = driver(**cisco_device)

# デバイスに接続
print("Connecting to the device...")
device.open()

# デバイスから情報を取得
print("\nGathering facts...")
facts = device.get_facts()
print(f"Facts: {facts}")

# インターフェース情報の取得
print("\nGetting interfaces...")
interfaces = device.get_interfaces()
for interface, details in interfaces.items():
    print(f"{interface}: {details}")

# 接続を閉じる
device.close()
print("\nDisconnected from the device.")
