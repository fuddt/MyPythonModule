import webbrowser
import configparser
from urllib.parse import urlencode
from OAuth2callback import MyHTTPServer
import requests

# サーバーを起動
my_http_server = MyHTTPServer()
my_http_server.start_server()

# 設定ファイルの読み込み
config = configparser.ConfigParser()
config.read('config.ini')

# OAuthプロバイダーの認証ページのURL
authorization_base_url = 'https://account.box.com/api/oauth2/authorize'

# アプリケーションのクライアントID（Box開発者コンソールから取得）
client_id = config['API_KEY']['CLIENT_ID']

# ステップ1で設定したリダイレクトURI
redirect_uri = 'http://127.0.0.1:8080/'

# 認証URLの生成
params = {
    'response_type': 'code',
    'client_id': client_id,
    'redirect_uri': redirect_uri,
}
# パラメータをURLに組み込む
auth_url = f"{authorization_base_url}?{urlencode(params)}"

# ユーザーにブラウザで認証URLを開くよう指示
print("Please go to the following URL and authorize the app:")
print(auth_url)

# ブラウザで自動的にURLを開く
webbrowser.open(auth_url)

# ブラウザでのユーザー操作を待つために簡単な入力を求める
input("After authorizing the app in the browser, press Enter to continue...")

# 取得した認証コード
authorization_code = my_http_server.get_code()

print(f"Authorization code: {authorization_code}")

# アプリケーションのクライアントIDとクライアントシークレット
client_id = config['API_KEY']['CLIENT_ID']
client_secret = config['API_KEY']['CLIENT_SECRET']

# アクセストークンを取得するためのエンドポイント
token_url = 'https://api.box.com/oauth2/token'

# POSTリクエストの本文に含めるデータ
data = {
    'grant_type': 'authorization_code',
    'code': authorization_code,
    'client_id': client_id,
    'client_secret': client_secret,
}

# アクセストークンを取得するためにPOSTリクエストを送信
response = requests.post(token_url, data=data)

# レスポンスからアクセストークンを取得
if response.status_code == 200:
    tokens = response.json()
    access_token = tokens['access_token']
    print("Access Token:", access_token)
    # 必要に応じてリフレッシュトークンも取得できます
    # refresh_token = tokens.get('refresh_token')
else:
    print("Error while retrieving the access token:", response.text)