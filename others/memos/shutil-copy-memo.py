import shutil
import os
import logging
from pathlib import Path

# ロギングの設定
logging.basicConfig(level=logging.DEBUG, filename='./file_copy.log', filemode='w',
                    format='%(asctime)s - %(levelname)s - %(message)s')

def custom_copy(src, dst):
    """カスタムコピー関数: エラーをキャッチして処理を続行し、ログに記録する"""
    try:
        shutil.copy2(src, dst)
    except Exception as e:
        logging.error(f"{src} : {e}")

def ignore_files(directory, files):
    """特定のファイルやディレクトリを無視する関数"""
    ignored = []
    dir_path = Path(directory)
    # ディレクトリパスに 'D' と 'sample' が含まれているかチェック
    if 'D' in dir_path.parts:
        for file in files:
            ignored.append(file)
        logging.info(f"Ignored files in directory {directory} because it contains 'D' and 'sample'")
    return ignored



def copy_files_with_logging(src, dst):
    """ファイルをコピーし、成功とエラーのログを生成する"""
    try:
        shutil.copytree(src, dst, ignore=ignore_files, copy_function=custom_copy, dirs_exist_ok=True)
    except Exception as e:
        logging.error(f"Error during copytree operation: {e}")

# コピーとログの出力
src_directory = "./test"
dst_directory = "./test_copy"
copy_files_with_logging(src_directory, dst_directory)
