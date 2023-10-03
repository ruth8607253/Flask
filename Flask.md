# Flask
## 環境建構
1. 開啟虛擬環境
2. 建構引入外部套件的環境(在裡面打Flask & 版本)

## 網站架構
```
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello</h1>aaaa"```

from flask import Flask：從flask引入一個叫做Flask的class

app：flask應用程式的實體

@app.route我要我的根目錄上有什麼

模擬是5000，真正是80

"/"：route()->decorator 註冊一個路徑：首頁
"/路徑" 新增一個網頁路徑

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello</h1>aaaa"

@app.route("/test")
def hellohello():
    return "<h1>bbbb</h1>"

我在終端機打flask --app test-f run --debug
出來http://127.0.0.1:5000
一開始開啟的介面是首頁 -> 顯示<h1>Hello</h1>aaaa

在http://127.0.0.1:5000後面打/test => http://127.0.0.1:5000/test
就會進到我新創的test頁面 -> 顯示<h1>bbbb</h1>

## 執行網站
`flask --app test-f run` 這個要關閉->重開

## 把做好的html連進python
1. 把要連過來的html裝進「templates」的資料夾裡
2. 在python寫以下程式

```from flask import render_template

@app.route('/')
def hello():
    return render_template('我創的html.html')```

from flask import render_template：引入html

return render_template('Hello.html')：回傳Hello.html裡的值

templates樣板

Static Files：圖片、CSS、JS

引入CSS：在html打

<link rel="stylesheet" href="{{url_for('static',filename='css/style.css')}}"> 

或是href="/static/css/style.css"

Jinja只能在template裡面使用