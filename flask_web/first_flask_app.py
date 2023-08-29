from flask import Flask, redirect, url_for
from datetime import datetime

app = Flask(__name__)


@app.route("/hello_user/<string:name>")
def hello_user(name):
    date = datetime.now()
    return f"<p>Hello, {name}! You have entered the site at {date}.</p>"


@app.route("/factorial/<number>")
def factorial_calculation(number: str):
    if number.isdigit():
        number = int(number)
        result = factorial(number)
        return f"<p>{result}</p>" if len(str(result)) < 20 else redirect(url_for("hello_user", name='Guest'))
    else:
        return redirect(url_for("exception", number=number))


@app.route("/exception/<number>")
def exception(number):
    return f"{number} - not a number. Enter number, not string!"


def factorial(number):
    if number < 2:
        return 1
    else:
        return number * factorial(number - 1)


if __name__ == '__main__':
    app.run(debug=True)
