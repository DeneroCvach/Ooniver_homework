from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('log_and_pass.html')
    else:
        data = request.form
        login = data['login']
        password = data['password']

        with open("login_data.txt", "w") as my_f:
            my_f.write(f"{login} {password}")

        return redirect(url_for('login', name=login))


@app.route
def hello():
    return render_template("hello.html")


if __name__ == '__main__':
    app.run(debug=True)
