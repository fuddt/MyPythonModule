""" """

import pathlib
current_dir = pathlib.Path(__file__).parent
file_name = "sample.txt"

# パスの結合 <現在ディレクトリ>/sample.txtを作る
# os.path.join()と違ってlinuxやmacOSでお馴染みのパスの区切り　/　で結合できる!!
path = current_dir / file_name
print(path)  # 出力 <現在ディレクトリ>\sample.txt

# パスからフォルダ名(ディレクトリ名)を取得する
dir_name = path.parent
print(dir_name)  # 出力 <現在ディレクトリ>

# パスからファイル名を取得する
file_name = path.name
print(file_name)  # 出力 sample.txt

# パスを分割する
dir_name, file_name = path.parent, path.name
print(dir_name)  # 出力 <現在ディレクトリ>
print(file_name)  # 出力 sample.txt


# ここからがpathlibにしかできないファイルの読み書き
# ファイルの読み込み

with path.open("w") as f:
    f.write("Hello, Python!")

# ファイルの書き込み
with path.open() as f:
    print(f.read())  # 出力 Hello, World!


# でも上記の記述はあまり見ないå、with open() as f: で書くことが多いです。
# with open(path, 'w') as f:
#     f.write('Hello, Python!')

# with open(path, 'r') as f:
#     print(f.read())  # 出力 Hello, Python!
