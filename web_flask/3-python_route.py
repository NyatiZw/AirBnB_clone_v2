#!/usr/bin/python3
'''Python Script to start a Flask web application'''

from flask import Flask

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
    """ setting defaults to route """

@app.route('/python/<text>', strict_slashes=False)
def python_with_text(text):
    """ Function to display Python and the dynamic text """
    text = text.replace('_', ' ')
    return f"Python {text}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
