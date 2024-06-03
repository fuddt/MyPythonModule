from boxsdk import OAuth2, Client, BoxAPIException
import configparser
import os
import hashlib

# config.iniからトークンとAPIキーを読み込む
config = configparser.ConfigParser()
config.read('./config.ini')

CLIENT_ID = config["API_KEY"]["CLIENT_ID"]
CLIENT_SECRET = config["API_KEY"]["CLIENT_SECRET"]
ACCESS_TOKEN = config["API_KEY"]["ACCESS_TOKEN"]
REFRESH_TOKEN = config["API_KEY"]["REFRESH_TOKEN"]

# OAuth2オブジェクトを作成
oauth2 = OAuth2(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    access_token=ACCESS_TOKEN,
    refresh_token=REFRESH_TOKEN,
)

# Boxクライアントを作成
client = Client(oauth2)

# アップロードするファイルのパス
file_path = 'sample.txt'

# ファイルのサイズを取得
size = os.stat(file_path).st_size

# ファイル名
file_name = os.path.basename(file_path)

# SHA-1ハッシュを計算する関数
def calculate_sha1(file_path):
    sha1 = hashlib.sha1()
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):
            sha1.update(chunk)
    return sha1.hexdigest()

try:
    # アップロード前のチェック
    file_id = None
    try:
        client.folder(folder_id='0').preflight_check(size=size, name=file_name)
    except BoxAPIException as e:
        if e.code == 'item_name_in_use':
            print(e.code)
            file_id = e.context_info['conflicts']['id']
        
    if file_id:
        uploaded_file = client.file(file_id).update_contents(file_path)
    else:
        # ファイルをアップロード
        uploaded_file = client.folder('0').upload(file_path=file_path, file_name=file_name)
        print(f'File "{uploaded_file.name}" uploaded successfully with file ID {uploaded_file.id}')
    
    # ローカルファイルのSHA-1ハッシュを計算
    local_sha1 = calculate_sha1(file_path)
    
    # アップロードされたファイルのSHA-1ハッシュを取得
    uploaded_sha1 = uploaded_file.sha1
    
    # ハッシュを比較
    if local_sha1 == uploaded_sha1:
        print("SHA-1 hash matches. File uploaded successfully.")
    else:
        print("SHA-1 hash does not match. There may be an issue with the upload.")
        print(f"Local SHA-1: {local_sha1}")
        print(f"Uploaded SHA-1: {uploaded_sha1}")

except BoxAPIException as e:
    print(f'Error: {e.message}')
    if e.context_info:
        print(e.context_info)
