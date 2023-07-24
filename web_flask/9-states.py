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


@app.route("/states", defaults={"id": None}, strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def list_states(id):
    """ list all State objects if no id else State obj with the id
    """
    state_objs = storage.all(State)
    objs = list()
    for obj_id, obj in state_objs.items():
        if id is not None:
            if obj_id.split(".")[1] == id:
                objs.append(obj)
                break
            else:
                continue
        objs.append(obj)
    # if object with specific id is not found, len of list == 0
    return render_template("9-states.html", states=objs)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
