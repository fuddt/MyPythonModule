import zipfile
import os
import glob

def zip_extract(dir_with_zip,to_dir=None):
    """
    summary:
    ディレクトリ内のzipファイルをすべて展開する。

    Args:
        dir_with_zip (str): zipファイルが入ったディレクトリ を指定
        to_dir (srt): 展開先ディレクトリ ->　指定がなければzipファイルが存在するディレクリに展開します。
    """
    if to_dir:
        pass
    else:
        to_dir = dir_with_zip
        
    dir_with_zip = os.path.join(dir_with_zip,'*.zip')
    filepaths = glob.glob(dir_with_zip)
    for filepath in filepaths:
        extractor = zipfile.ZipFile(filepath)
        extractor.extractall(to_dir)
