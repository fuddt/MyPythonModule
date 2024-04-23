import shutil
import logging
from pathlib import Path

# ロギング設定
logging.basicConfig(filename='copytree.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def custom_error_handler(func, path, exc_info):
    """
    カスタムエラーハンドラー
    エラー情報をログに記録します。
    
    :param func: 発生した例外を呼び出した関数
    :param path: エラーが発生したファイルのパス
    :param exc_info: 例外情報のタプル
    """
    logging.error(f"エラーが発生しました: {path}")
    logging.error(f"例外情報: {exc_info}")

def copy_directory(source, destination):
    """
    ディレクトリをコピーする関数です。エラーが発生した場合、カスタムエラーハンドラを使用してログに記録します。
    
    :param source: コピー元のディレクトリパス
    :param destination: コピー先のディレクトリパス
    """
    try:
        shutil.copytree(Path(source), Path(destination), onerror=custom_error_handler)
        logging.info(f"{source} から {destination} へのコピーが完了しました。")
    except Exception as e:
        logging.error(f"ディレクトリのコピー中に未処理のエラーが発生しました: {e}")

# 使用例
source_directory = "/path/to/source"
destination_directory = "/path/to/destination"
copy_directory(source_directory, destination_directory)


def custom_error_handler(func, path, exc_info):
    """
    カスタムエラーハンドラー
    エラー情報をログに記録した後、処理を続行します。
    
    :param func: 発生した例外を呼び出した関数
    :param path: エラーが発生したファイルのパス
    :param exc_info: 例外情報のタプル
    """
    logging.error(f"エラーが発生しました: {path}")
    logging.error(f"例外情報: {exc_info}")
    # 例外を無視して処理を続行
    return
    
import os
import shutil
import logging

# ロギングの設定
logging.basicConfig(filename='copy_errors.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def custom_error_handler(func, path, exc_info):
    """
    カスタムエラーハンドラー
    発生したエラーをログに記録し、処理を続行します。
    
    :param func: 発生した例外を呼び出した関数
    :param path: エラーが発生したファイルのパス
    :param exc_info: 例外情報のタプル
    """
    logging.error(f"エラーが発生しました: {path}, {exc_info[1]}")
    # 例外を無視して処理を続行
    return

def copy_directory(source, destination):
    """
    ディレクトリをコピーします。エラーが発生してもログに記録し、残りのファイルのコピーは続けます。
    
    :param source: コピー元のディレクトリパス
    :param destination: コピー先のディレクトリパス
    """
    if not os.path.exists(destination):
        os.makedirs(destination)
    for item in os.listdir(source):
        src_path = os.path.join(source, item)
        dst_path = os.path.join(destination, item)
        try:
            if os.path.isdir(src_path):
                shutil.copytree(src_path, dst_path, onerror=custom_error_handler)
            else:
                shutil.copy2(src_path, dst_path)
        except Exception as e:
            # 既にエラーハンドラで記録されているエラーのため、ここでは特に処理は不要
            pass

# 使用例
source_directory = "/path/to/source"
destination_directory = "/path/to/destination"
copy_directory(source_directory, destination_directory)

