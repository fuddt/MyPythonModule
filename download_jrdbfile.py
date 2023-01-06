import os,sys
sys.path.append(os.pardir)
from settings import JRDB_PASS, JRDB_ID,GECKODRIVER_PATH
import requests
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import urllib
import zipfile
"""
JRDBの会員ページから最新のPACIとSEDをzipファイルをダウンロードして展開するmodule
IDとPASSは別ファイルから取得する
"""

class DL_ZIP_FROM_JRDB(object):
    def __init__(self):
        service = Service(executable_path=GECKODRIVER_PATH)
        browser = webdriver.Firefox(service=service)
        browser.get(f'http://{JRDB_ID}:{JRDB_PASS}@www.jrdb.com/member/n_index.html')
        time.sleep(5)
        #JRDBデータをクリックして、最新データページへ移動する
        browser.find_element(By.LINK_TEXT,'ＪＲＤＢデータ').click()
        time.sleep(1)
        browser.find_element(By.XPATH,'/html/body/div[1]/div[15]/div[2]/div[7]/div/div[2]/a[1]').click()
        time.sleep(2)
        #現在操作中のwindow（またはタブ）
        current_window = browser.current_window_handle
        #現在開いているwindowたち
        windows = browser.window_handles
        #もし現在のwindow以外のものがあればそっちに切り替える。
        for window in windows:
            if window != current_window:
                browser.switch_to.window(window)
                break

        #現在のURLの取得
        url = browser.current_url
        # BeautifulSoupでファイルのダウンロードを行う。
        req = requests.get(url)
        soup = BeautifulSoup(req.content, 'html.parser')

        self.url = url
        self.soup = soup
        self.browser = browser
           
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

    # tagからzipファイルのダウンロードurlを取得する
    def get_zip_url(self, tag):
        """
        １行目:zipファイルは上記で見つけたタグの４つ先のタグになる。
        ２行目:タグ内の属性値の取り出し。タグ内に属性があると辞書型で属性:値という構成で返してくれる。
        """
        zipfile_tag = tag[0].find_next().find_next().find_next().find_next()
        zipurl = zipfile_tag.attrs['href']
        return zipurl

    def zip_download(self, zipurl, savedir_name, to_dir = None):
        # zipfileのlinkURLが相対パスになっているので、絶対パスに直す urllibを使用
        zipurl = urllib.parse.urljoin(self.url, zipurl)
        if to_dir == None:
            to_dir = os.getcwd()

        #ファイルのDLはrequests.get(zipファイルのurl)でDL可能
        zipreq = requests.get(zipurl)
        #zipファイルの保存
        with open(savedir_name,'wb') as f:
            for chunk in zipreq.iter_content(chunk_size=100000):
                if chunk:
                    f.write(chunk)
        #zipファイルの展開
        extractor = zipfile.ZipFile(savedir_name)
        extractor.extractall(to_dir)

def download_jrdb_zipfile(savedir,todir):
    try:
        dl_zip_from_jrdb = DL_ZIP_FROM_JRDB()
        time.sleep(2)
        #SEDのzipファイルを探す。
        sed_zip_tag = dl_zip_from_jrdb.search_ziptag('JRDB成績速報データ(SED)')
        #PACIのzipファイルを探す。
        paci_zip_tag = dl_zip_from_jrdb.search_ziptag('JRDBデータパック(PACI)')
        #zipファイルのURLの取得
        sed_zip_url = dl_zip_from_jrdb.get_zip_url(sed_zip_tag)
        paci_zip_url = dl_zip_from_jrdb.get_zip_url(paci_zip_tag)
        #zipのDLと展開
        dl_zip_from_jrdb.zip_download(sed_zip_url, savedir , todir)
        #一応、待機
        time.sleep(2)
        dl_zip_from_jrdb.zip_download(paci_zip_url, savedir, todir)
        #すべての処理が終わり次第、ブラウザを閉じる
        dl_zip_from_jrdb.browser.close()
    except Exception as e:
        print(e,'\nエラーが発生しました。')
        dl_zip_from_jrdb.browser.close()