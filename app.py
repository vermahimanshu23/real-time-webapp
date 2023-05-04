from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug .utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__)

app.secret_key = 'your secret key'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'realtime'

mysql = MySQL(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(
            'SELECT * FROM users WHERE email = % s AND password = % s', (email, password, ))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['id'] = account['id']
            session['email'] = account['email']
            msg = 'Logged in successfully !'
            return render_template('test.html', msg=msg)
        else:
            msg = 'Incorrect email / password !'
    return render_template('login.html', msg=msg)


@app.route('/whyus')
def whyus():
    return render_template('whyus.html')


@app.route('/support')
def support():
    return render_template('support.html')


@app.route('/test')
def test():
    return render_template('test.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
