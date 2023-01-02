import zipfile
import os
import glob

def zipExtractorMeantForInDir(dir_with_zip,to_dir):
    """
    summary:
    ディレクトリ内のzipファイルをすべて展開します。

    Args:
        dir_with_zip (str): zipファイルが入ったディレクトリ 
        to_dir (srt): 展開先ディレクトリ
    """
    dir_with_zip = os.path.join(dir_with_zip,'*.zip')
    filepaths = glob.glob(dir_with_zip)
    for filepath in filepaths:
        extractor = zipfile.ZipFile(dir_with_zip)
        extractor.extractall(to_dir)