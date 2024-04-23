import os
import shutil
import logging

# ロギングの設定
logging.basicConfig(filename='copy.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def custom_error_handler(func, path, exc_info):
    """
    カスタムエラーハンドラ
    重複するファイルがあった場合にログに記録し、例外を無視して処理を続行します。
    
    :param func: 発生した例外を呼び出した関数
    :param path: エラーが発生したファイルのパス
    :param exc_info: 例外情報のタプル
    """
    if exc_info[0] == FileExistsError:
        logging.info(f'重複スキップ: {path}')
    else:
        # その他のエラーはログに記録して再度例外を発生させる
        logging.error(f'エラー発生: {path}, {exc_info}')
        raise exc_info[1]

def copy_directory(source, destination):
    """
    ディレクトリをコピーします。重複するファイルがあった場合にはスキップし、ログに記録します。
    
    :param source: コピー元のディレクトリパス
    :param destination: コピー先のディレクトリパス
    """
    try:
        shutil.copytree(source, destination, ignore=shutil.ignore_patterns('*'), onerror=custom_error_handler)
    except Exception as e:
        logging.error(f'コピー中にエラーが発生しました: {e}')

# 使用例
source_directory = "/path/to/source"
destination_directory = "/path/to/destination"
copy_directory(source_directory, destination_directory)