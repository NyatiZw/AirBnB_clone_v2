#!/usr/bin/python3
'''Python Script to start a Flask web application'''

from flask import Flask, render_template, g
from models import storage
from models.state import State
from sqlalchemy.orm import scoped_session
from sqlalchemy import inspect

app = Flask(__name__)
app.url_map.strict_slashes = False

#Creaate a session for each request
@app.before_request
def before_request():
    g.session = scoped_session(storage._Session)
    g.session.expire_on_commit = False

#Close the session after each request
@app.teardown_request
def teardown_request(exception=None):
    session = getattr(g, 'session', None)
    if session is not None:
        session.remove()

@app.route('/cities_by_states')
def cities_by_states():
    states = g.session.query(State).order_by(State.name).all()
    return render_template('7-cities_by_states.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
