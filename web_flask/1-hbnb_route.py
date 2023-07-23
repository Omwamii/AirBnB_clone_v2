#!/usr/bin/python3
""" script to start Flask web app with 2 routes
"""
from flask import Flask

app = Flask(__name__)

# Route to display "Hello HBNB!"
@app.route("/", strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"

# Route to display "HBNB"
@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
