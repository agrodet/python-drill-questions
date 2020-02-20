# Python基礎ドリル　問題コード集

2020-02-20

Grodet Aymeric、松本　翔太、新居　雅行 [link](/https://lifematics.co.jp "ライフマティックス株式会社")

---

- オーム社より2020年に発売された『Python基礎ドリル』の問題プログラムのファイルを公開します。
- ここでは問題となる完成されていないコードのみのを公開します。問題を公開してはいません。

## 利用方法

問題は、章ごとに、問題番号がわかるファイル名でまとめてあります。開いて穴埋め部分を書き直し、実行して確認等ができます。

穴埋め部分は、書籍の中では、丸数字（①など）を横長のボックスで囲っていますが、問題ごとのファイルでは、1番目の穴埋めは """①"""、2番目の穴埋めは """②""" のように、丸数字を3つのダブルクォートで囲った表示にしてあります。問題によっては穴埋め部分を書き直さないと実行できない場合もありますが、それが文字列の中のような場合にはそのまま実行できてしまう場合もあります。後者の場合は、もちろん、自分で書き換えを行ってください。

### repl.itで利用される場合

repl.itの「import repo」ボタンをクリックし、「Import From GitHub」を選択して、レポジトリのURLとして、ここのURL、つまり

https://github.com/agrodet/python-drill-questions

を入力してください。すると、1つのReplが新たに作られて、そこにこのレポジトリのファイルが全部展開されています。

このレポジトリのルートにある.replitファイルを利用して、読み込まれたReplでは常に、ルートにあるall_start_replit.pyが実行されるようになっています。このファイルは初期状態では、Chapter_1フォルダのall_questions.pyファイルをインポートしています。all_questions.pyファイルを参照すると、Q1_01.pyファイルをインポートする部分があり、基本的にコードがある問題のファイルが全てインポートされています。しかしながら、多くはコメントになっています。初期状態では、単にQ1_01.pyファイルのプログラムが動くだけになります。最初の問題からかかる方は、そのままQ1_01.pyを修正して、望む動作になるように変更しましょう。

別の問題のプログラムを動かしたい場合、その問題のコメントを外します。例えば、Chapter1_1/all_questions.pyファイルにある「from . import Q1_02」の行頭にある#を消して保存します。そして、Runを実行すると、Q1_02.pyが実行されます。また、Chapter_2を進めたいなら、ルートにあるall_start_replit.pyを開き、「from Chapter_2 import all_questions.py」の行のコメントを外します。Chapter_2/all_questions.pyでは、Q2_01だけが実行されるようになっているので、別の問題に切り替えたい場合には、all_questions.pyのコメントを変更すれば良いでしょう。このように、章単位、問題単位で実行したいものだけをコメントがない状態にすることで、単一の問題ごとに実行ができます。もちろん、既に終わったものはコメントに入れないでも構いません。そこは自由に利用してください。

### IDEで利用される場合

それぞれのファイルを開いて、そのファイルを実行するように操作すれば良いでしょう。all_start_replit.pyや、Chapter_X/all_questions.pyファイルについては、無視していただいて構いません。