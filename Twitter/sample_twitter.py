import configparser
import requests
from requests_oauthlib import OAuth1


conf = configparser.ConfigParser()
conf.read('config.ini', encoding='utf-8')

# 認証情報
consumer_key = conf['TwitterAPI']['CONSUMER_KEY']
consumer_secret = conf['TwitterAPI']['CONSUMER_SECRET']
access_token = conf['TwitterAPI']['ACCESS_TOKEN']
access_token_secret = conf['TwitterAPI']['ACCESS_TOKEN_SECRET']

# OAuth1 セッションを作成
auth = OAuth1(consumer_key, 
              consumer_secret, 
              access_token, 
              access_token_secret)

# エンドポイントURL
url = "https://api.twitter.com/2/tweets"

# 投稿するツイートの内容
payload = {"text": "Hello World!"}

# リクエストを送信
response = requests.post(url, json=payload, auth=auth)

# 応答を確認
if response.status_code == 201:
    print("ツイート成功!")
    print(response.json())
else:
    print(f"Error: {response.status_code} - {response.text}")
