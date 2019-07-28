### Atcoder用のディレクトリ・ファイル作成
①「user_info.py」に自分のユーザー情報と言語IDを設定する。対応言語は現在のところpythonのみ。

    USERNAME='hogehoge'
    PASSWORD='hogehoge'

    # 言語ID
    CPP_ID = 3023　# python


②コンソールで以下のコマンドを実行（ex.ABC093を作成したい場合）


    python mkdir.py abc 086
以下の構成でディレクトリとファイルが作成される。

    .
    └── ABC
        └── 093
            ├── A.py
            ├── B.py
            ├── C.py
            └── D.py




---

### テスト実施〜提出〜ジャッジ結果の取得
①コンソールで以下のコマンドを実行（ex.「/ABC/093/C.py」を提出したい場合）。


    python testnsub.py abc 093 c
    
②コンソールにテスト結果が出力され、提出するかどうかを標準入力で問われる。


    [提出ファイル]
    /hogehoge/ABC/093/C.py
    ************************************************************
    [入力例 1]
    2 5 4
    [出力例 1]
    2
    [あなたの出力]
    2
    ************************************************************
    [入力例 2]
    2 6 3
    [出力例 2]
    5
    [あなたの出力]
    5
    ************************************************************
    [入力例 3]
    31 41 5
    [出力例 3]
    23
    [あなたの出力]
    23
    ************************************************************
    [3/3]
    提出しますか？(y/n)

③提出したくない場合は「n」を入力し、リターンしてください。処理終了します。
提出したい場合は「y」を入力し、リターンしてください。提出したのち、ジャッジ結果を取得します。

    y
    提出完了しました.
    結果を取得します.
    　　　　　　　 　.i||||||||||||||||||||||||||||||i.　　　　　　　　　　　　　..ii||||||||||!!!!||||||||||||||||||||||||| 
    　　　　　　　　.i| !||||||||||||||||||||||||||||||i. 　　　　　　　　 　..ii|||||||||||||!　ii||||||||||||||||||||||||||| 
    　　　　　　　 i|| 　!||||||||||||||||||||||||||||||i. 　　　　　　　 .i||||||||||||||||!　 i||||||||||||||||||||||||||||| 
    　　　　　 　 i|| 　　.!||||||||||||||||||||||||||||||i.　　　　　　.ii||||||||||||||||!! 　 .||||||||||||||||||||||||||||| 
    　　　　　　i|||　　　　!||||||||||||||||||||||||||||||i.　　 　　.i|||||||||||||||||||i　　　!||||||||||||||||||||||||||| 
    　　　　　 i|||| 　　　 　!||||||||||||||||||||||||||||||i.　　　.||||||||||||||||||||||i.　　　　!||||||||||||||||||||||| 
    　　　　 i||||||||.　　　　　!||||||||||||||||||||||||||||||i.　　 |||||||||||||||||||||||||ii.. 
    　　　 i||||||||||||i. 　　　　 !||||||||||||||||||||||||||||||i.　　|||||||||||||||||||||||||||||ii.. 
    　　. i||||||||||||||||||i 　　　　!||||||||||||||||||||||||||||||i. 　 !||||||||||||||||||||||||||||||||iiii.. 
    　　.||||||||||||||||||||||||||||||||. .!||||||||||||||||||||||||||||||i.　　 ||||||||||||||||||||||||||||||||||||||||||||||||||||||| 
    　　||||||||||||||||||||||||||||||||| 　!||||||||||||||||||||||||||||||i.　　!||||||||||||||||||||||||||||||||||||||||||||||||||||| 
    　　.||||||||||||||||||||||||||||||||　　!||||||||||||||||||||||||||||||i. 　　!|||||||||||||||||||||||||||||||||||||||||||||||||| 
    　　. !|||||||||||||||||||||||||||||| 　　!||||||||||||||||||||||||||||||i. 　　　.!||||||||||||||||||||||||||||||||||||||||||||| 
    　　　 !||||||||||||||||||||||||||||　　　!||||||||||||||||||||||||||||||i. 　　　　 .!|||||||||||||||||||||||||||||||||||||||| 
    　　　　　.!||||||||||||||||||||||| 　　　.!||||||||||||||||||||||||||||||i. 　　　　　　　.!!|||||||||||||||||||||||||||||| 