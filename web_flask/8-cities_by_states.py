#!/usr/bin/python3
""" Script to list states from db
"""
from models import storage
from models.state import State
from flask import Flask, escape, render_template

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(res_or_except):
    """ remove the currenct SQLAlchemy session
    """
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def list_cities_by_states():
    """ list all State objects in DBStorage sorted
    """
    state_objs = storage.all(State)
    objs = list()
    for obj_id, obj in state_objs.items():
        objs.append(obj)
    return render_template("8-cities_by_states.html", states=objs)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
