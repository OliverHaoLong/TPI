from app import app
from flask import Flask, render_template

@app.route('/hello')
def hello():
    return "Hello, World!"
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
