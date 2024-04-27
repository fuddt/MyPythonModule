
# ファイル操作の基本 pathを生成する

  

パスの生成でよく使われる標準ライブラリー

  

os<br>

pathlib

  

どちらでもパスを生成することができます

  

### なにが違うの？

  

## os.path と pathlib の比較

<ol>

<li>コードのスタイルと読みやすさ：<br>

pathlib はモダンなオブジェクト指向スタイルを採用しており、パスをオブジェクトとして扱います。これにより、メソッドチェーンやプロパティを使った直感的な操作が可能です。<br>

os.path はより伝統的な関数ベースのアプローチで、パスを文字列として扱います。これは長い間Pythonで使用されており、広く理解されていますが、操作がやや冗長になることがあります。<br>

</li>

パスを結合するというコードで比較してみます。
```
import  os

# フォルダとファイル名を設定 
folder  =  "/Users/user/Desktop"
file_name  =  "sample.txt"

# Pathオブジェクトを作成して、ファイル名を結合 
join_path  =  os.path.join(folder, file_name)

# 結合したパスを表示  
print(join_path)
>>> /Users/user/Desktop/sample.txt
```
```
import  pathlib

# フォルダとファイル名を設定
# pathilb.Pathオブジェクトを作成
folder  =  pathlib.Path("/Users/user/Desktop")
file_name  =  "sample.txt"

# Pathオブジェクトを使用して、ファイル名を結合
# パスの区切りで使用する’/’でパスの結合を表現できて直感的な記述ができるのが特徴
join_path  =  folder / file_name   

# 結合したパスを表示
print(join_path)
>>> /Users/user/Desktop/sample.txt
```


<br>

<li>
機能性：

pathlib は os.path の機能をほぼ全てカバーしており、<u><strong>それに加えてファイルやディレクトリの作成、読み書きなどの追加メソッドを提供します。</strong></u><br>

例えば、Path オブジェクトを直接開いて読み書きすることができ、これは os.path では直接はできません。<br>

os.path はパス操作に特化しており、ファイルの存在確認や属性取得などのためには他の os モジュールの関数と組み合わせて使用します。

</li>

</ol>

  

pathlib はよりモダンで直感的なAPIを提供し、コードの可読性と書きやすさを向上させるため、多くの新しいPythonプロジェクトで好まれています。

<br>

<br>

  

# 一緒に覚えて欲しい \_\_file\_\_

  

### __file__とは?

実行されたスクリプトファイルのパスを取得することができます！

  

...と言われても何のこっちゃ？何が便利なの？と思われるかもしれません。<br>

<br>

  

たとえばあるプログラムで以下のようなものを作成したとします。

- ユーザーが入力した文字列をテキストファイルに出力する

- 出力場所はスクリプトファイル output_text.pyと同じディレクトリ内

<br>

<br>

  

上記を満たすプログラムを以下のように作成したとします。

```

#ユーザーの入力を待つ

user_input = input('文字を入力してね: ')

 
# 出力先を相対パスでスクリプトファイルと同じディレクトリ内

path = "./output.txt"
 

# テキストファイルに出力する

with open(path, 'w') as f:

f.write(user_input)

```

"ファイル出力のためのサンプルコード"で上記のようなコードが紹介されるのをよく見ますが、実用的ではありません。<br>

<br>

相対パスの ./ を使えば、スクリプトと同じディレクトリにファイルを出力できると思われがちですが、この場合、<strong>"スクリプトを実行した場所を基準"</strong>に同一ディレクトリに出力されます。

<br>

例えば

このスクリプトが以下のディレクトリにあったとします。<br>

<code>/Users/user/Desktop/myPython/myModule/output_text/output_text.py
</code>


スクリプトを実行しよう！と思った時に、ターミナルを開いて

```

cd /Users/user/Desktop/myPython/myModule/output_text

python output_text.py

```

とcdを使って移動してから実行したとします。
この手順であればスクリプトと同じディレクトリ内にテキストファイルが出力されます。

ですが、以下のように実行した場合

```

python ~/Desktop/myPython/myModule/output_text/output_text.py

```

この場合、`~/`直下に出力されてしまいます。<br>

<br>

相対パスは<br>

"スクリプトがある場所を起点"とするのではなく<br>

"<u><strong>スクリプトを実行した場所</strong></u>を起点"とするからです。

<br>

これでは少し不便ですね。スクリプトを実行するのが、必ずスクリプトがある場所で行われるとは限らないからです。
そこで便利なのが__file__です。<br>

<br>

# __file__の活用事例<br>

__file__は、Pythonスクリプトが実行されているファイルの名前（フルパス）を持つ組み込み変数です。<br>

とりあえず難しい言葉は抜きにこれだけ覚えていればOKです<br>

<u><i><strong>「スクリプトが存在するディレクトリを取得することができる」</u></i></strong><br>

<br>

これにより、スクリプトが存在するディレクトリに依存しないコードを書くことが可能になります。


# 何はともあれ体験してみる!

  

２つのファイル出力のためのスクリプトを用意しました。

  

<code>use/use__file__.py</code><br>

->_file__を使ったスクリプト

  

<code>not_use/not_use__file__.py</code><br>

->__file__を使わずに相対パスのみで作成したスクリプト

  

上記を<code>what_is__file__</code>ディレクトリで実行してみてください<br>

<code>python use/use__file__.py<br></code>

<code>python not_use/not_use__file__.py</code>

  

それぞれoutput.txtが出力された位置を確認してみてください

  

`__file__`を使ったスクリプトでは<code>use__file__.py</code>と同じフォルダ内に作成されます。<br>

<code>not_use__file__</code>.pyは<code>what_is__file__</code>ディレクトリ内に作成されてしまうのがわかると思います。<br>

<br>

what_is__file__ディレクトリをダウンロードして実行してみてください 。
<ol>
<li>what_is__file__ディレクトリを任意の場所にダウンロードする</li>
<li>ダウンロードしたzipを展開する</li>
<li>ターミナルを開いて<br>
cd を使ってwaht_is__file__に移動する</li>
<li>python use/use__file__.py　</li>
<li>python not_use/not_use__file__.py</li>

</ol>
それぞれoutput.txtが出力された位置を確認してみてください
__file__を使ったスクリプトではuse__file__.pyと同じフォルダ内に作成されます。
not_use__file__.pyはwhat_is__file__ディレクトリ内に作成されてしまうのがわかると思います。
