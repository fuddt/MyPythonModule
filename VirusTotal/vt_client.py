import configparser
import requests

# 独自の例外クラス
class VirusTotalAPIError(Exception):
    """VirusTotal APIエラー"""

class VtClient:
    """VirusTotal APIクライアントクラス"""
    API_URL = "https://www.virustotal.com/api/v3"
    
    def __init__(self) -> None:
        """コンストラクタ
        
        Args:
            api_key (str): VirusTotal APIキー
        """

        config = configparser.ConfigParser()
        config.read("config.ini")
        self.api_key = config["API_KEY"]["API_KEY"]
        self.analysis_data = None
        self.headers = {
            "accept": "application/json",
            "x-apikey": self.api_key
        }
        self.url = None

    def _post_request(self, endpoint: str, data=None) -> dict:
        """POSTリクエストを送信する
        
        Args:
            endpoint (str): エンドポイント
            data (dict): 送信データ
        
        Returns:
            dict: レスポンスJSON
        """
        url = f"{self.API_URL}/{endpoint}"
        if data:
            response = requests.post(url, headers=self.headers, data=data)
        else:
            response = requests.get(url, headers=self.headers)
        return response.json()

    def _url_id(self, url: str) -> dict:
        """URLのIDを取得する
        
        Args:
            url (str): URL
        
        Returns:
            dict: URLのID
        """
        data = {"url": url}
        json_response = self._post_request("urls", data=data)
        return json_response["data"]["id"]

    def url_analysis(self, url: str) -> None:
        """URLの解析を行う
        
        Args:
            url (str): 解析するURL
        
        Returns:
            None
        """
        self.url = url
        url_id = self._url_id(url)
        endpoint = f"analyses/{url_id}"
        response_json = self._post_request(endpoint)
        self.analysis_data = response_json["data"]["attributes"]["stats"]

    def get_detection(self, detection_type: str) -> int:
        """検出数を取得する
        
        Args:
            detection_type (str): 検出タイプ
        
        Returns:
            int: 検出数
        """
        if self.analysis_data is None:
            return None
        return self.analysis_data.get(detection_type, None)

    def malicious(self) -> int:
        """悪意のある検出数を取得する"""
        return self.get_detection("malicious")

    def suspicious(self) -> int:
        """疑わしい検出数を取得する"""
        return self.get_detection("suspicious")

    def harmless(self) -> int:
        """無害な検出数を取得する"""
        return self.get_detection("harmless")

    def undetected(self) -> int:
        """未検出数を取得する"""
        return self.get_detection("undetected")

    # 上記の内容をまとめてターミナルに表示する
    def print_analysis(self) -> None:
        """解析結果を表示する"""
        if self.analysis_data is None:
            raise VirusTotalAPIError("解析データがありません")
        print(f"{self.url} の解析結果")
        print(f"悪意のある検出数: {self.malicious()}")
        print(f"疑わしい検出数: {self.suspicious()}")
        print(f"無害な検出数: {self.harmless()}")
        print(f"未検出数: {self.undetected()}")
    
    def output_report(self, output_file: str) -> None:
        """解析結果をファイルに出力する
        
        Args:
            output_file (str): 出力ファイル名
        
        Returns:
            None
        """
        if self.analysis_data is None:
            raise VirusTotalAPIError("解析データがありません")
        
        with open(output_file, "w") as f:
            f.write(f"{self.url} の解析結果\n")
            f.write(f"悪意のある検出数: {self.malicious()}\n")
            f.write(f"疑わしい検出数: {self.suspicious()}\n")
            f.write(f"無害な検出数: {self.harmless()}\n")
            f.write(f"未検出数: {self.undetected()}\n")
            

if __name__ == "__main__":
    vt_client = VtClient()
    vt_client.url_analysis("https://www.google.com")
    vt_client.print_analysis()