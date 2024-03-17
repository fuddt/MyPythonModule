import tweepy
import configparser

configparser = configparser.ConfigParser()
# 認証情報を設定ファイルから読み込む
configparser.read('config.ini', encoding='utf-8')
consumer_key = configparser["TwitterAPI"]["CONSUMER_KEY"]
consumer_secret = configparser["TwitterAPI"]["CONSUMER_SECRET"]
access_token = configparser["TwitterAPI"]["ACCESS_TOKEN"]
access_token_secret = configparser["TwitterAPI"]["ACCESS_TOKEN_SECRET"]
bearer_token = configparser['TwitterAPI']['BEARER_TOKEN']

# OAuthHandler オブジェクトを作成
client = tweepy.Client(bearer_token=bearer_token,
                          consumer_key=consumer_key,
                          consumer_secret=consumer_secret,
                          access_token=access_token,
                          access_token_secret=access_token_secret)

client.create_tweet(text="Hello world", user_auth=True)