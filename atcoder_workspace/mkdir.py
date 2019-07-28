import requests
from time import sleep
from bs4 import BeautifulSoup
import sys
import config
import os.path
import login

# 実行時引数を取得
args = sys.argv
# abc,arc,agc etc...
level = args[1].upper()
# ex. 080,091,111
round = args[2].zfill(3)
# カレントディレクトリのパス
wd = os.getcwd()

# ファイル作成
new_dir_path = '{wd}/{level}/{round}'.format(
    wd=wd,
    level=level,
    round=round
)
if not os.path.exists(new_dir_path):
    os.makedirs(new_dir_path)

if level == 'ABC':
    prob_list = ['A', 'B', 'C', 'D', 'E', 'F']
else:
    prob_list = ['A', 'B', 'C', 'D', 'E', 'F']

# ログイン
login.login()
# 問題ページのURLを取得
task_url = "https://atcoder.jp/contests/{level}{round}/tasks".format(
    level=level,
    round=round
)
html = config.SESSION.get(task_url)
soup = BeautifulSoup(html.text, 'lxml')
a = soup.select('a')
plob_path_map = {}
for ai in a:
    try:
        text = ai.get_text()
        if text in prob_list:
            link = ai.attrs['href']
            plob_path_map[text] = link
    except:
        pass

for prob in prob_list:
    print('[{prob}問題]'.format(prob=prob))
    new_file_path = '{new_dir_path}/{prob}.py'.format(
        new_dir_path=new_dir_path,
        prob=prob
    )

    prob_url = "https://atcoder.jp{prob_path}".format(prob_path=plob_path_map[prob])
    print(prob_url)
    print(new_file_path)

    html = config.SESSION.get(prob_url)
    soup = BeautifulSoup(html.text, 'lxml')
    tags = soup.select('pre')
    fl = tags[0].text.strip()
    format_line_list = fl.split('\r\n')
    lines = []
    lines.append('import sys')
    lines.append('input = sys.stdin.readline')
    for format_line in format_line_list:
        input_format = format_line.split()
        line = ""
        if '_' not in input_format[0] and ':' not in input_format[0] and '\\vdots' not in input_format[0]:
            if len(input_format) == 1:
                # 入力が1文字の場合
                if input_format[0] == 'S':
                    line = input_format[0].lower() + ' = input()'
                else:
                    line = input_format[0].lower() + ' = int(input())'
            else:
                # それ以外
                cnt = 0
                for input in input_format:
                    if cnt >= 1:
                        line += ', '
                    line += input.lower()
                    cnt += 1
                line += ' = map(int, input().split())'
            lines.append(line)

    with open(new_file_path, "w") as f:
        for line in lines:
            print(line, file=f)
    print()
