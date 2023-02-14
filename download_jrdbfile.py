import os
import requests
import time
from bs4 import BeautifulSoup
import urllib
import zipfile
import inspect
import os
import glob

JRDB_ID = "*******"
JRDB_PASSWORD = "*******"

class DownloadFlowZipFileFromJRDB(object):
    def __init__(self):
        #現在のURLの取得
        url = (f'http://{JRDB_ID}:{JRDB_PASS}@www.jrdb.com/member/data/')
        # BeautifulSoupでファイルのダウンロードを行う。
        req = requests.get(url)
        soup = BeautifulSoup(req.content, 'html.parser')
        self.url = url
        self.soup = soup

    def search_ziptag(self, tag_text):
        """
        tdを全部取得。
        SEDのZIPファイルがあるのは JRDB成績速報データ(SED)
        PACIのZIPファイルがあるのは　JRDBデータパック(PACI)のテキストがある場所。
        """
        ziptag = []
        for tag in self.soup.find_all('td'):
            if tag.text == tag_text:
                ziptag.append(tag)
        return ziptag
    
    def select_zip(self,ziptag):
        ind = None
        if len(ziptag) > 1:
            items = [tag.find_previous().find_previous().find_previous().text for tag in ziptag]
            print(ziptag[0])
            for num,item in enumerate(items):
                print(num,item)    
            ind = int(input('please choose one'))
            if ind > len(items):
                raise ValueError('選択肢以外の数字が入りました。')
        if ind == None:
            ind =0
        return int(ind)
    

    # tagからzipファイルのダウンロードurlを取得する
    def get_zip_url(self, tag):
        """
        １行目:zipファイルは上記で見つけたタグの４つ先のタグになる。
        ２行目:タグ内の属性値の取り出し。タグ内に属性があると辞書型で属性:値という構成で返してくれる。
        """
        
        ind = self.select_zip(tag)
        
        zipfile_tag = tag[ind].find_next().find_next().find_next().find_next()
        zipurl = zipfile_tag.attrs['href']
        return zipurl

    def zip_download(self, zipurl, savefile_name):
        # zipfileのlinkURLが相対パスになっているので、絶対パスに直す urllibを使用
        zipurl = urllib.parse.urljoin(self.url, zipurl)
        #ファイルのDLはrequests.get(zipファイルのurl)でDL可能
        zipreq = requests.get(zipurl)
        #zipファイルの保存
        with open(savefile_name,'wb') as f:
            for chunk in zipreq.iter_content(chunk_size=100000):
                if chunk:
                    f.write(chunk)


class DownLoadJRDBZipFile(object):
    def __init__(self):
        filename = inspect.getfile( inspect.currentframe() ) # module file name
        self.dirpath = os.path.dirname(filename)
        self.store_dir = os.path.join(self.dirpath,'PACI')
    
    def download_jrdb_zipfile(self, store_dir = None):
        if store_dir:
            self.store_dir = store_dir
        else:
            pass

        dl_zip_from_jrdb = DownloadFlowZipFileFromJRDB()
        time.sleep(2)
        #SEDのzipファイルを探す。
        sed_zip_tag = dl_zip_from_jrdb.search_ziptag('JRDB成績速報データ(SED)')
        #PACIのzipファイルを探す。
        paci_zip_tag = dl_zip_from_jrdb.search_ziptag('JRDBデータパック(PACI)')
        #zipファイルのURLの取得
        sed_zip_url = dl_zip_from_jrdb.get_zip_url(sed_zip_tag)
        paci_zip_url = dl_zip_from_jrdb.get_zip_url(paci_zip_tag)
        #zipのDL
        dl_zip_from_jrdb.zip_download(sed_zip_url, os.path.join(self.store_dir,'SED.zip'))
        time.sleep(2)#一応、待機
        dl_zip_from_jrdb.zip_download(paci_zip_url, os.path.join(self.store_dir,'PACI.zip'))


    def zip_extract(self):
        #zipファイルの展開
        filepaths = glob.glob(os.path.join(self.store_dir, '*.zip'))
        for filepath in filepaths:
            extractor = zipfile.ZipFile(filepath)
            extractor.extractall(os.path.dirname(filepath))
            #zipファイルの削除
            os.remove(filepath)
