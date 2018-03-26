from app import app
from flask import Flask, url_for

@app.route('/hello')
def hello()
    return "Hello, World!"
@app.route('/')
@app.route('/index')
def index():
    url_for("/www/index.html")
