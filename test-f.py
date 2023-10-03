from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('test-f.html')

@app.route("/test")
def hellohello():
    return "<h1>bbbb</h1>"