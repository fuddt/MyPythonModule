import shutil

# Copy file
shutil.copy('sample.txt', 'sample_copy.txt')

# Copy directory
shutil.copytree('sample_dir', 'sample_dir_copy')

# Move file
shutil.move('sample.txt', 'sample_move.txt')

# Remove file
shutil.rmtree('sample_dir_copy')

# Remove directory
# ignore_errors=Trueを指定することでエラーが発生しても無視して削除を続行する
shutil.rmtree('sample_dir_move', ignore_errors=True)

# shutil.copytreeの引数ignoreを使って特定のファイルをコピーしないようにする
def ignore_file(dir, files):
    """txtファイルのみコピーする"""
    return [f for f in files if f.endswith('.txt')]
shutil.copytree('sample_dir', 'sample_dir_copy', ignore=ignore_file)

# shutil.copytreeのcopy_function引数を使ってファイルのコピー方法を変更する
def copy_file(src, dst):
    """txtファイルのみコピーする"""
    if src.endswith('.txt'):
        shutil.copy2(src, dst)

shutil.copytree('sample_dir', 'sample_dir_copy', copy_function=copy_file)

# shutil.copytreeのcopy_function引数を使ってファイルのコピー方法を変更するpart2
# エラーが発生した場合は無視してコピーを続行する
def copy_file(src, dst):
    """errorが発生しても無視してコピーを続行する"""
    try:
        shutil.copy2(src, dst)
    except Exception as e:
        print(f"Error: {e}")

shutil.copytree('sample_dir', 'sample_dir_copy', copy_function=copy_file)