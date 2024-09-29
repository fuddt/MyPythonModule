import webbrowser
import configparser
import http.server
import socketserver
from urllib.parse import urlparse, parse_qs
import threading
import requests

class OAuth2CallbackHandler(http.server.SimpleHTTPRequestHandler):
    code = None  # 認証コードを保持するクラス変数
    
    def do_GET(self):
        # クエリパラメータから認証コードを取得
        query_components = parse_qs(urlparse(self.path).query)
        code = query_components.get('code')
        
        # 認証コードが既に取得されている場合は上書きしない
        if code and not self.__class__.code:
            self.__class__.code = code
            print(f"Authorization code received: {self.__class__.code}")
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"Authentication successful. You can close this window.")
        elif not code:
            # 認証コードが含まれていないリクエストは無視（ただし、codeが既に設定されている場合は何もしない）
            print("Request without code received; ignoring.")
        else:
            # 認証コードが既に取得されているが、別のリクエストが来た場合
            print("Authorization code already received; ignoring further requests.")
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"Authorization code already received.")


def start_server(port=8080):
    with socketserver.TCPServer(("", port), OAuth2CallbackHandler) as httpd:
        print(f"Serving HTTP on 0.0.0.0 port {port} (http://0.0.0.0:{port}/)...")
        httpd.serve_forever()

# パラメータをURLに組み込む
from urllib.parse import urlencode
# サーバーを別スレッドで起動
threading.Thread(target=start_server, daemon=True).start()
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

auth_url = f"{authorization_base_url}?{urlencode(params)}"

# ユーザーにブラウザで認証URLを開くよう指示
print("Please go to the following URL and authorize the app:")
print(auth_url)
# ブラウザで自動的にURLを開く
webbrowser.open(auth_url)

# サーバーが起動した後、ブラウザでのユーザー操作を待つために簡単な入力を求める
input("After authorizing the app in the browser, press Enter to continue...")
# アプリケーションのクライアントIDとクライアントシークレット
client_id = config['API_KEY']['CLIENT_ID']
client_secret = config['API_KEY']['CLIENT_SECRET']


# アクセストークンを取得するためのエンドポイント
token_url = 'https://api.box.com/oauth2/token'

# ステップ2で取得した認証コード
authorization_code = OAuth2CallbackHandler.code

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
