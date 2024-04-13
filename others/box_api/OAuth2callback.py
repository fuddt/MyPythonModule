import http.server
import threading
from urllib.parse import urlparse, parse_qs

class OAuth2CallbackHandler(http.server.SimpleHTTPRequestHandler):
    code = None  # インスタンス変数として認証コードを保持

    def do_GET(self) -> None:
        """GETリクエストを処理するメソッド"""
        query_components = parse_qs(urlparse(self.path).query)
        code = query_components.get('code', [None])[0]
            
        if code is not None:
            OAuth2CallbackHandler.code = code  # インスタンス変数に認証コードを保持
            print(f"Authorization code received: {self.code}")
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"Authentication successful. You can close this window.")



class MyHTTPServer():
    def __init__(self, port=8080) -> None:
        self.port = port
        self.handler_instance = None

    def _http_server(self):
        """OAuth2CallbackHandlerを使ってHTTPサーバーを起動するメソッド"""
        def handler(*args, **kwargs) -> OAuth2CallbackHandler:
            """OAuth2CallbackHandlerのインスタンスを生成する関数"""
            self.handler_instance = OAuth2CallbackHandler(*args, **kwargs)
            return self.handler_instance

        with http.server.HTTPServer(("", self.port), handler) as httpd:
            print(f"サーバーを起動しました。ポート番号: {self.port}")
            httpd.serve_forever()

    def start_server(self) -> None:
        """HTTPサーバーを別スレッドで起動するメソッド"""
        threading.Thread(target=self._http_server, daemon=True).start()

    def get_code(self) -> None | str:
        """認証コードを取得するメソッド"""
        return self.handler_instance.code  # リストの最初の要素を返す
