from netmiko import ConnectHandler

def netmiko_connect(host, username, password):
    # デバイスの情報を定義
    device = {
        'device_type': 'cisco_ios',
        'host': host,
        'username': username,
        'password': password,
    }

    # SSH接続
    connection = ConnectHandler(**device)
    
    # コマンドを実行
    output = connection.send_command('show ip interface brief')
    print(output)

    # 接続を閉じる
    connection.disconnect()

host = "https://sandboxapicdc.cisco.com"
username = "admin"
password = "!v3G@!4@Y"
netmiko_connect(host, username, password)
