import os
import tarfile
import gzip
import zipfile
import glob

def extract_file(directory_path, extract_to='.'):
    filepaths = glob.glob(directory_path)

    for filepath in filepaths:
        # Get the base filename from the filepath
        filename = os.path.basename(filepath)

        """指定されたファイルを解凍する。対応形式: .gz, .tar, .tar.gz, .zip"""
        if filepath.endswith('.tar.gz') or filepath.endswith('.tgz'):
            with tarfile.open(filepath, 'r:gz') as tar:
                tar.extractall(path=extract_to)
        elif filepath.endswith('.tar'):
            with tarfile.open(filepath, 'r:') as tar:
                tar.extractall(path=extract_to)
        elif filepath.endswith('.gz'):
            with gzip.open(filepath, 'rb') as f_in:
                with open(filepath[:-3], 'wb') as f_out:
                    f_out.write(f_in.read())
        elif filepath.endswith('.zip'):
            with zipfile.ZipFile(filepath, 'r') as zip_ref:
                zip_ref.extractall(extract_to)
        else:
            print(f".gz, .tar, .tar.gz, .zipのいずれでもないファイル: {filename}")

# Example usage
