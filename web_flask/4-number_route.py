#!/usr/bin/python3
"""
Flask web application
"""
from flask import Flask
import sys


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hbnb():
    """
        display Hello HBNB
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb_():
    """
        display HBNB
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def hbnb_c(text):
    """
        display a text
    """
    txt = text.replace('_', ' ')
    return 'C {}'.format(txt)


@app.route('/number/<int:n>', strict_slashes=False)
def hbnb_n(n):
    """
        display an integer
    """
    return '{} is a number'.format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
