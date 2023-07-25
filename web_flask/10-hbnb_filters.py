#!/usr/bin/python3
""" Script to list states from db
"""
from models import storage
from models.state import State
from models.amenity import Amenity
from flask import Flask, escape, render_template

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(res_or_except):
    """ remove the currenct SQLAlchemy session
    """
    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def display_hbnb():
    """ display full style hbnb page with State, City, Amenity objects
    """
    amenities = storage.all(Amenity)
    amenity_objs = list()
    for am_id, obj in amenities.items():
        amenity_objs.append(obj)
    states = storage.all(State)
    state_objs = list()
    for state_id, obj in states.items():
        state_objs.append(obj)
    return render_template("10-hbnb_filters.html", states=state_objs,
                           amenities=amenity_objs)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
