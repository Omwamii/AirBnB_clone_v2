#!/usr/bin/python3
""" Script to list states from db
"""
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
from flask import Flask, escape, render_template

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(res_or_except):
    """ remove the currenct SQLAlchemy session
    """
    storage.close()


@app.route("/hbnb", strict_slashes=False)
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
    places = storage.all(Place)
    place_objs = list()
    for place_id, obj in places.items():
        place_objs.append(obj)
    return render_template("100-hbnb.html", states=state_objs,
                           amenities=amenity_objs, places=place_objs)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
