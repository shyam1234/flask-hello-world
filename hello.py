# Shamelessly copied from http://flask.pocoo.org/docs/quickstart/
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"
