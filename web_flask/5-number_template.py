#!/usr/bin/python3

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/number_template/<int:n>')
def number_template_n(n):
    return render_template('5-number.html', n=n)


@app.route('/number/<int:n>')
def number_n(n):
    return '{} is a number'.format(n)


@app.route('/python/')  # , defaults={'text': 'is cool'})
@app.route('/python/<text>')
def python_text(text="is cool"):
    return 'Python ' + text.replace('_', ' ')


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
