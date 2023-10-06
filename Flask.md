# Flask
一個架網站的地方。可以架靜態 & 動態網站。
## 特性
1. 偵錯：html或python哪裡寫錯會紅字。
2. 有python測試介面。
3. 可以用Jinja。
4. 支援萬國碼。
5. 免錢。

[連結](https://seanyeh.medium.com/python-web-%E5%BF%AB%E9%80%9F%E5%BB%BA%E7%BD%AE%E7%B6%B2%E7%AB%99%E7%9A%84flask%E5%A5%97%E4%BB%B6-59318830bd63)
## 環境建構
1. 開啟虛擬環境
2. 建構引入外部套件的環境(在裡面打Flask & 版本)
## 網站架構
```
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello</h1>aaaa"
```

`from flask import Flask`：從flask引入一個叫做Flask的class

`app`：flask應用程式的類別實體

`__name__`：就是`__name__ == "__main__"`那個，將`__name__`傳給Flask

`@app.route("/")`：下面的函式要載入到哪個url位址中 => 根目錄。

return `"<h1>Hello</h1>aaaa"` ：回傳引號裡的值(到頁面)。

網頁末4碼：模擬是5000，真正是80

`"/"：route()->decorator`：註冊一個路徑-首頁
`"/路徑"` 新增一個網頁路徑

```
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello</h1>aaaa"

@app.route("/test")
def hellohello():
    return "<h1>bbbb</h1>"
```

在終端機打`flask --app test-f run --debug`

出來`http://127.0.0.1:5000`

一開始開啟的介面是首頁 -> 顯示`<h1>Hello</h1>aaaa`

在`http://127.0.0.1:5000後面打/test` => `http://127.0.0.1:5000/test`

就會進到我新創的test頁面 -> 顯示`<h1>bbbb</h1>`

## 執行網站
`flask --app test-f run` 這個要關閉->重開

## 把做好的html連進python
1. 把要連過來的html裝進「templates」的資料夾裡
2. 在python寫以下程式

```
from flask import render_template

@app.route('/')
def hello():
    return render_template('我創的html.html')
```

`from flask import render_template`：引入html

`return render_template('Hello.html')`：回傳Hello.html裡的值

templates：樣板

`Static Files`：圖片、CSS、JS

引入CSS：在html打

`<link rel="stylesheet" href="{{url_for('static',filename='css/style.css')}}"> `

或是`href="/static/css/style.css"`，但不推薦用這個。這樣以後如果突然想改放在不同資料夾裡的效果還要去查路徑、改，讓程式去找比較實在。

## 網頁b裡開一個連結，把在.py裡的網頁a連到裡面
在網頁裡面打：

`<p><a href="{{url_for('網頁a的def名')}}">超連結名稱</a></p>`

範例：

網頁a：
```
@app.route("/test")
def hellohello():
    return "<h1>bbbb</h1>"
```

在網頁b的html裡打：

`<p><a href="{{url_for('hellohello')}}">bbb</a></p>`

## Jinja
1. 只能在template裡面使用。
2. 有些地方只能用單引號。
3. 基本語法：
    1. {{XXX}} 輸出寫法 e.g.href="{{url_for('static',filename='css/bootstrap.css')}}" -> 將static/css/bootstrap.css裡的css設定輸出給該html。
    2. {%XXX%} 描述語法 e.g.{% extends "base.jinja.html" %} -> 描述：繼承base.jinja.html的所有語法
