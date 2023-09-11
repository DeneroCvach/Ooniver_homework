from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route("/redirect_test/<string:role>")
def check_role(role):
    if role == 'admin':
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('guest', role=role))


@app.route("/admin")
def admin():
    return f"<p>Hello, Admin!</p>"


@app.route("/guest/<role>")
def guest(role):
    return f"<p>Hello, guest, you enter like a {role}!</p>"


if __name__ == '__main__':
    app.run(port=5002)
