#!/usr/bin/python3
'''Python Script to start a Flask web application'''

from flask import Flask, render_template, g
from models import storage
from models.state import State
from models.city import City
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

@app.route('/states')
def states():
    states = g.session.query(State).order_by(State.name).all()
    return render_template('9-states.html', states=states)

@app.route('/states/<string:state_id>')
def state_detail(state_id):
    state = g.session.query(State).get(state_id)
    if state:
        return render_template('state_detail.html', state=state)
    else:
        return render_template('not_found.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
