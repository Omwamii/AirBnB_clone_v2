#!/usr/bin/python3
""" script with route rules
"""
from flask import Flask, escape, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_with_text(text):
    text = text.replace('_', ' ')
    return f"C {escape(text)}"


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_with_text(text="is cool"):
    text = text.replace('_', ' ')
    return f"Python {escape(text)}"


@app.route("/number/<int:n>", strict_slashes=False)
def number_is_integer(n):
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    return render_template("5-number.html", number=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
