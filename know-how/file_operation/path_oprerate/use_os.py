"""
osモジュールを使ってパス操作を行う
"""

import os

# パスの結合 C:/Users/user/Desktopを作る
current_dir = os.path.dirname(__file__)
file_name = "sample.txt"

# パスを結合する
path = os.path.join(current_dir, file_name)
print(path)  # 出力 <現在ディレクトリ>\sample.txt

# パスからフォルダ名(ディレクトリ名)を取得する
dir_name = os.path.dirname(path)
print(dir_name)  # 出力 <現在ディレクトリ>

# パスからファイル名を取得する
file_name = os.path.basename(path)
print(file_name)  # 出力 sample.txt

# パスを分割する
dir_name, file_name = os.path.split(path)
print(dir_name)  # 出力 <現在ディレクトリ>
print(file_name)  # 出力 sample.txt
