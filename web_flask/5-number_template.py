#!/usr/bin/python3

"""
    A Flask web application that listens on
    0.0.0.0 port 5000 and returns messages on
    different routes
"""

from flask import Flask, render_template

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


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    """ displays n if it's only an integer """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_number_on_page(n):
    """ renders a page displaying the number provided """
    return render_template('5-number.html', num=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
