import requests
from bs4 import BeautifulSoup
import user_info
import config


def login():
    LOGIN_URL = "https://atcoder.jp/login"

    # セッション開始
    session = requests.session()

    # csrf_token取得
    r = session.get(LOGIN_URL)
    s = BeautifulSoup(r.text, 'lxml')
    csrf_token = s.find(attrs={'name': 'csrf_token'}).get('value')

    # ログイン情報を設定
    login_info = {
        "csrf_token": csrf_token,
        "username": user_info.USERNAME,
        "password": user_info.PASSWORD
    }

    result = session.post(LOGIN_URL, data=login_info)
    result.raise_for_status()
    if result.status_code == 200:
        config.SESSION = session
        config.CSRF_TOKEN = csrf_token
    else:
        print("ログイン失敗")
        exit()
