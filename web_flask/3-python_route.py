#!/usr/bin/python3

"""
    A Flask web applications tha listens on
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


@app.route('/c/<text>', strict_slashes=False)
def ciswhat(text):
    """ returns C + <user text> for the specified route """
    return "C " + text.replace("_", " ")


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniswhat(text="is cool"):
    """ returns Python + <user text> for the specified route """
    return "Python " + text.replace("_", " ")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
