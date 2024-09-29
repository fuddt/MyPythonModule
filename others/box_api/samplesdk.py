from boxsdk import OAuth2
import webbrowser

CLIENT_ID = 'YOUR_CLIENT_ID'
CLIENT_SECRET = 'YOUR_CLIENT_SECRET'
REDIRECT_URI = 'http://localhost'  # 適切なリダイレクトURIを設定

oauth2 = OAuth2(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    store_tokens=None,
)

auth_url, csrf_token = oauth2.get_authorization_url(REDIRECT_URI)

# Webブラウザで認証URLを開く
webbrowser.open(auth_url)

# 認証後にリダイレクトされたURLからコードを取得
auth_code = input('Enter the authorization code: ')

access_token, refresh_token = oauth2.authenticate(auth_code)