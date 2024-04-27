import sqlite3
import mysql.connector

class DatabaseAdapter:
    """データベース操作の共通インターフェース"""
    def connect(self):
        pass
    def execute(self, query):
        pass

class SQLiteAdapter(DatabaseAdapter):
    """SQLiteデータベースへのアダプター"""
    def __init__(self, dbname):
        self.dbname = dbname
        self.connection = None

    def connect(self):
        self.connection = sqlite3.connect(self.dbname)

    def execute(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()
        return cursor.fetchall()

class MySQLAdapter(DatabaseAdapter):
    """MySQLデータベースへのアダプター"""
    def __init__(self, host, user, password, dbname):
        self.host = host
        self.user = user
        self.password = password
        self.dbname = dbname
        self.connection = None

    def connect(self):
        self.connection = mysql.connector.connect(host=self.host, user=self.user, password=self.password, database=self.dbname)

    def execute(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()
        return cursor.fetchall()

# クライアントコード
def database_query(adapter, query):
    """データベースに接続してクエリを実行する汎用関数"""
    adapter.connect()
    result = adapter.execute(query)
    print(result)

# 使用例
sqlite_adapter = SQLiteAdapter('test.db')
database_query(sqlite_adapter, "SELECT * FROM example_table")

mysql_adapter = MySQLAdapter('localhost', 'user', 'password', 'test_db')
database_query(mysql_adapter, "SELECT * FROM example_table")
