"""
__file__を使う場合のサンプルコード

__file__とpathlib(もしくはos.path)を使ってファイルを出力する

上記を行うことで、ファイルの出力場所を
このスクリプトが存在する場所を基準にしてファイルを出力することができる

つまり、このスクリプトをどこで実行してもいつも同じ場所にファイルを出力することができる

"""
import pathlib

path = pathlib.Path(__file__).parent / 'sample.txt'

with open(path, 'w') as f:
    f.write('Hello, World!')
    

# # 以下はos.pathを使う場合のサンプルコード
# import os 

# path = os.path.join(os.path.dirname(__file__), 'sample.txt')

# with open(path, 'w') as f:
#     f.write('Hello, World!')