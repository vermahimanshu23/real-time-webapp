from flask import Flask, render_template, request, redirect
from werkzeug .utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    gender = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.name


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def form_view():
    if request.method == 'POST':
        with app.app_context():
            name = request.form['name']
            email = request.form['email']
            password = request.form['password']
            gender = request.form['gender']
            print(name)
            print(email)
            print(password)
            print(gender)
            # Perform database operations here using SQLAlchemy, for example:
            users = User.query.all()
            print(users)
    return render_template('login.html')


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
