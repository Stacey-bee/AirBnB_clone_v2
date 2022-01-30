#!/usr/bin/python3

"""
    A Flask web applications that listens on
    0.0.0.0 port 5000 and returns messages on
    different routes
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_index():
    """ triggered function from the / route """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    """ triggered function from the /hbnb route """
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
