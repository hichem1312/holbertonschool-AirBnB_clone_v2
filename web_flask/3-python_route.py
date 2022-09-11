#!/usr/bin/python3
"""
flask web application
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
        g
    """
    txt = text.replace('_', ' ')
    return 'C {}'.format(txt)


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def hbnb_p(text="is cool"):
    """
        display a text
    """
    txt = text.replace('_', ' ')
    return 'Python {}'.format(txt)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
