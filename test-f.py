from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")

def hello(name):
    return f"Hello, {name}."

@app.route("/<name>")
def hellohello(name):
    data={
        "name":name,
        "age":18,
        "location":"Taiwan",
    }
    return render_template('test-f.html',**locals())