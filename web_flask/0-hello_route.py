#!/usr/bin/python3
"""
mode flask
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hbnb():
    """
        hbnb route
    """
    return 'Hello HBNB!'


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
