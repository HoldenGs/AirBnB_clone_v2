#!/usr/bin/python3

from flask import Flask
app = Flask(__name__)


@app.route('/c/<text>')
def c_text(text):
    return 'C ' + text.replace('_', ' ')


@app.route('/hbnb')
def hbnb():
    return 'HBNB'


@app.route('/')
def hello_hbnb():
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
