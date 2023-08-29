from flask import Flask, redirect, render_template, request

app = Flask(__name__)


@app.route('/')
def main_form():
    return render_template('forms.html')


@app.route('/vibe', methods=['GET'])
def vibe():
    data = request.args
    vibe = data['vibe']
    return f'Ваше настроение - {vibe}'


@app.route('/info', methods=['POST'])
def info():
    data = request.form
    name = data['name']
    age = data['age']
    gender = data['gender']
    return f'{name} {age} {gender}'


if __name__ == '__main__':
    app.run(debug=True)
