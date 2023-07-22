#!/usr/bin/python3
'''Python Script to start a Flask web application'''

from models import storage
from models import *
from flask import Flask, render_template

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
    return f"C {text}"


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_with_text(text):
    """ Function to display Python and the dynamic text """
    text = text.replace('_', ' ')
    return f"Python {text}"


@app.route('/number/<int:n>', strict_slashes=False)
def number_is_interger(n):
    """ Function to displlay number """
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ Function to display number template """
    return render_template('number_template.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """ Function to display html if number even """
    odd_or_even = 'even' if n % 2 == 0 else 'odd'
    return render_template(
        'template/6-number_odd_or_even.html',
        number=n,
        odd_or_even=odd_or_even
    )


@app.teardown_appcontext
def tear_down(self):
    """Remove current session """
    storage.close()


@app.route('/states_list')
def html_fetch_states():
    """Display html """
    state_obj = [s for s in storage.all("State").value()]
    return render_template(
        '7-state_list.html',
        state_obj=state_obj
    )


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
