#!/usr/bin/python3
'''Python Script to start a Flask web application'''

from flask import Flask, render_template
from models import storage
from models.state import State
from sqlalchemy.orm import scoped_session
from sqlalchemy import inspect

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.before_request
def before_request():
    g.session = scoped_session(storage._Session)
    g.session.expire_on_commit = False

@app.teardown_request(exception=None):
    session = getattr(g, 'session', None)
    if session is not None:
        session.remove()

@app.route('/states_list')
def states_list():
    states = g.session.query(State).order_by(State.name).all()
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
