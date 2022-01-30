#!/usr/bin/python3

"""
    A Flask web applications that listens on
    0.0.0.0 port 5000 and returns the message
    'Hello HBNB!'
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ triggered function that returns our message """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
