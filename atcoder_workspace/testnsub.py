import subprocess
from bs4 import BeautifulSoup
from time import sleep
import sys
import config
import user_info
import os.path
import login
import re

# 実行時引数を取得
args = sys.argv
# abc,arc,agc etc...
level = args[1].upper()
# 080,101 etc...
round = args[2].zfill(3)
# a,b,c,d etc...
prob = args[3].upper()
# カレントディレクトリのパス
wd = os.getcwd()

# 提出するソースのパスを作成
target_file_url = '{wd}/{level}/{round}/{prob}.py'.format(
    wd=wd,
    level=level,
    round=round,
    prob=prob
)
print('[提出ファイル]')
print(target_file_url)
if level == 'ABC':
    prob_list = ['A', 'B', 'C', 'D', 'E', 'F']
else:
    # ABC以外はF問題まであると仮定
    prob_list = ['A', 'B', 'C', 'D', 'E', 'F']

if prob not in prob_list:
    # ユーザの入力した問題がユーザの入力したコンテストのレベルの問題に存在しない場合、処理終了
    print("Problem '{prob}' doesn't exist in {level}".format(level=level, prob=prob))
    exit()

# ログイン
login.login()

# ------------------------------test part start----------------------------------

# 「問題」ページのurlを作成
tasks_url = "https://atcoder.jp/contests/{level}{round}/tasks".format(level=level, round=round)

# 「問題」ページを取得
html = config.SESSION.get(tasks_url)
soup = BeautifulSoup(html.text, 'lxml')
a = soup.select('a')
plob_path_map = {}
for ai in a:
    try:
        # aタグのテキストを取得
        text = ai.get_text()
        if text in prob_list:
            # テキストの文字列が問題リストに含まれていた場合、aタグのhref属性を取得
            link = ai.attrs['href']
            # 問題とリンクをマッピング
            plob_path_map[text] = link
    except:
        pass

if prob not in plob_path_map:
    # ユーザが入力した問題のリンクが取得できなかった場合
    print("問題のリンクの取得に失敗しました. '{level}{round}{prob}'".format(level=level, round=round, prob=prob))
    exit()

# 問題文ページのurlを作成
prob_url = "https://atcoder.jp{prob_path}".format(prob_path=plob_path_map[prob])
# 問題文ページを取得
html = config.SESSION.get(prob_url)
soup = BeautifulSoup(html.text, 'lxml')
tags = soup.select('pre')
tags.pop(0)
input_tags = tags[0::2]
output_tags = tags[1::2]
exe_cnt = len(input_tags) // 2
ac_cnt = 0
for i in range(exe_cnt):
    print('************************************************************')
    input_example = input_tags[i].text.strip()
    output_example = output_tags[i].text.strip()

    p = subprocess.Popen('python ' + target_file_url, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    your_output = p.communicate(input_example.encode('utf-8'))[0]
    your_output = your_output.decode('utf-8').strip()
    print('【入力例 {num}】'.format(num=i + 1))
    print(input_example)
    print('【出力例 {num}】'.format(num=i + 1))
    print(output_example)
    print('【あなたの出力】')
    print(your_output)
    if your_output == output_example:
        ac_cnt += 1

print('************************************************************')
print('【{ac_cnt}/{exe_cnt}】'.format(ac_cnt=str(ac_cnt), exe_cnt=str(exe_cnt)))

# ------------------------------test part end----------------------------------
# ------------------------------submit part start------------------------------
print("提出しますか？(y/n)")
while True:
    answer = input()
    if answer.lower() == 'n':
        # nなら処理終了
        exit()
    elif answer.lower() == 'y':
        break

# 提出ソースコードの読み込み
if os.path.exists(target_file_url):
    f = open(target_file_url)
    source_code = f.read()  # ファイル終端まで全て読んだデータを返す
    f.close()
else:
    # 提出ソースが存在しない場合、処理終了
    print("ファイルが見つかりません." + target_file_url)
    exit()

# 提出情報作成
prob_path = plob_path_map[prob]
task_screen_name = prob_path[prob_path.rfind('/') + 1:]
submit_info = {
    "data.TaskScreenName": task_screen_name,
    "csrf_token": config.CSRF_TOKEN,
    "data.LanguageId": user_info.CPP_ID,
    "sourceCode": source_code
}
# 「提出」ページのURL取得
submission_url = "https://atcoder.jp/contests/{level}{round}/submit".format(level=level, round=round)

# 提出情報を送信
result = config.SESSION.post(submission_url, data=submit_info)
result.raise_for_status()
if result.status_code == 200:
    print("提出完了しました.")
else:
    print("提出に失敗しました.")

# ------------------------------submit part end------------------------------
# ------------------------------judge part start-----------------------------
print("結果を取得します.")
for _ in range(36):
    # 5秒ごとに結果を取りに行く
    sleep(5)
    # 「自分の提出」ページのURL作成
    my_submission_url = "https://atcoder.jp/contests/{level}{round}/submissions/me".format(level=level, round=round)
    # ログイン時に作成したセッションで「自分の提出」ページ取得
    html = config.SESSION.get(my_submission_url)
    soup = BeautifulSoup(html.text, 'lxml')
    # 一番新しいレコード
    tr = soup('tr')[1]
    # 判定結果セルのテキストを取得
    result_text = tr.find(class_=re.compile("label label-")).get_text().strip()
    if result_text == 'AC':
        print("\r", end="")

        print('　　　　　　　 　.i||||||||||||||||||||||||||||||i.　　　　　　　　　　　　　..ii||||||||||!!!!||||||||||||||||||||||||| ')
        print('　　　　　　　　.i| !||||||||||||||||||||||||||||||i. 　　　　　　　　 　..ii|||||||||||||!　ii||||||||||||||||||||||||||| ')
        print('　　　　　　　 i|| 　!||||||||||||||||||||||||||||||i. 　　　　　　　 .i||||||||||||||||!　 i||||||||||||||||||||||||||||| ')
        print('　　　　　 　 i|| 　　.!||||||||||||||||||||||||||||||i.　　　　　　.ii||||||||||||||||!! 　 .||||||||||||||||||||||||||||| ')
        print('　　　　　　i|||　　　　!||||||||||||||||||||||||||||||i.　　 　　.i|||||||||||||||||||i　　　!||||||||||||||||||||||||||| ')
        print('　　　　　 i|||| 　　　 　!||||||||||||||||||||||||||||||i.　　　.||||||||||||||||||||||i.　　　　!||||||||||||||||||||||| ')
        print('　　　　 i||||||||.　　　　　!||||||||||||||||||||||||||||||i.　　 |||||||||||||||||||||||||ii.. ')
        print('　　　 i||||||||||||i. 　　　　 !||||||||||||||||||||||||||||||i.　　|||||||||||||||||||||||||||||ii.. ')
        print('　　. i||||||||||||||||||i 　　　　!||||||||||||||||||||||||||||||i. 　 !||||||||||||||||||||||||||||||||iiii.. ')
        print('　　.||||||||||||||||||||||||||||||||. .!||||||||||||||||||||||||||||||i.　　 ||||||||||||||||||||||||||||||||||||||||||||||||||||||| ')
        print('　　||||||||||||||||||||||||||||||||| 　!||||||||||||||||||||||||||||||i.　　!||||||||||||||||||||||||||||||||||||||||||||||||||||| ')
        print('　　.||||||||||||||||||||||||||||||||　　!||||||||||||||||||||||||||||||i. 　　!|||||||||||||||||||||||||||||||||||||||||||||||||| ')
        print('　　. !|||||||||||||||||||||||||||||| 　　!||||||||||||||||||||||||||||||i. 　　　.!||||||||||||||||||||||||||||||||||||||||||||| ')
        print('　　　 !||||||||||||||||||||||||||||　　　!||||||||||||||||||||||||||||||i. 　　　　 .!|||||||||||||||||||||||||||||||||||||||| ')
        print('　　　　　.!||||||||||||||||||||||| 　　　.!||||||||||||||||||||||||||||||i. 　　　　　　　.!!|||||||||||||||||||||||||||||| ')

        import pygame.mixer as m
        import time

        m.init(47000)
        m.music.load("AC.wav")
        m.music.play()
        m.music.play(1)
        time.sleep(10)  # 音楽の再生時間
        m.music.stop()  # 再生の終了
        break
    elif result_text == 'WA' or result_text == 'CE' or result_text == 'TLE' \
            or result_text == 'MLE' or result_text == 'RE' or result_text == 'OLE' \
            or result_text == 'IE':
        print("\r【{result_text}】".format(result_text=result_text), end="")
        break
    else:
        print("\r【{result_text}】".format(result_text=result_text), end="")
# ------------------------------judge part end-----------------------------
