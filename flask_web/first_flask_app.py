from flask import Flask, redirect, url_for
from datetime import datetime

app = Flask(__name__)


@app.route("/first_flask_app/<string:name>")
def hello_user(name):
    date = datetime.now()
    return f"<p>Hello, {name}! You have entered the site at {date}.</p>"


@app.route("/first_flask_app/factorial/int:<number>")
def factorial_calculation(number):
    if type(number) == int:
        result = factorial(number)
        return f"<p>{result}</p>"
    else:
        return redirect(url_for("exception"))


@app.route("/exception")
def exception():
    raise TypeError("Enter number, not string!")


def factorial(number):
    if number < 2:
        return 1
    else:
        return number * factorial_calculation(number - 1) if len(str(number)) < 20 \
            else redirect(url_for("first_flask_app"))


if __name__ == '__main__':
    app.run(debug=True, port=5000)
