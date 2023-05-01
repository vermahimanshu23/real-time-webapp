from flask import Flask, render_template, request, redirect
from werkzeug .utils import secure_filename

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/registration', methods=['GET', 'POST'])
def form_view():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        gender = request.form['gender']
        print(name)
        print(email)
        print(password)
        print(gender)
    return render_template('user_registration.html')


@app.route('/login')
def login():
    return render_template('user_login.html')


@app.route('/whyus')
def whyus():
    return render_template('whyus.html')


@app.route('/services')
def services():
    return render_template('services.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
