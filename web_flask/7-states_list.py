#!/usr/bin/python3
'''Python Script to start a Flask web application'''

from flask import Flask, render_template
from models import storage
from models import *

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Function that displays Hello HBNB """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Function that displays HBNB """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_with_text(text):
    """ Function that displays text and
        removes the "_" with a space
    """
    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_with_text(text="is cool"):
    """ Function to display Python and the dynamic text """
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number_is_interger(n):
    """ Function to displlay number """
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ Function to display number template """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """ Function to display html if number even """
    odd_or_even = 'even' if (n % 2 == 0) else 'odd'
    return render_template(
        '6-number_odd_or_even.html',
        n=n,
        odd_or_even=odd_or_even
    )


@app.teardown_appcontext(strict_slashes=False)
def tear_down(self):
    """remove current SQLAlchemy session"""
    storage.close()


@app.route('/states_list', strict_slashes=False))
def fetch_states():
    """Display html page"""
    state_objs = [s for s in storage.all("State").values()]
    return render_template('7-states_list.html',
                           state_objs=state_objs)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
