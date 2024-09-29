import json
import csv
import xml.etree.ElementTree as et

class DataReader:
    """ファイルからデータを読み込むための共通インターフェース"""
    def read_data(self):
        pass

class JSONReader(DataReader):
    """JSON形式のファイルを読み込む具体的なアダプター"""
    def __init__(self, filename):
        self.filename = filename

    def read_data(self):
        with open(self.filename, 'r') as file:
            return json.load(file)

class CSVReader(DataReader):
    """CSV形式のファイルを読み込む具体的なアダプター"""
    def __init__(self, filename):
        self.filename = filename

    def read_data(self):
        with open(self.filename, newline='') as file:
            return list(csv.reader(file))

class XMLReader(DataReader):
    """XML形式のファイルを読み込む具体的なアダプター"""
    def __init__(self, filename):
        self.filename = filename

    def read_data(self):
        tree = et.parse(self.filename)
        root = tree.getroot()
        return [{child.tag: child.text for child in element} for element in root]

# クライアントコード
def client_code(reader):
    """DataReaderインターフェースを通じてファイルからデータを読み込むクライアント関数"""
    data = reader.read_data()
    print(data)

# JSONファイルからのデータ読み込み
json_reader = JSONReader('data.json')
client_code(json_reader)

# CSVファイルからのデータ読み込み
csv_reader = CSVReader('data.csv')
client_code(csv_reader)

# XMLファイルからのデータ読み込み
xml_reader = XMLReader('data.xml')
client_code(xml_reader)
