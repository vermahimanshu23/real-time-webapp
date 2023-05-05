from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug .utils import secure_filename
import re

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')



@app.route('/support', methods=['GET', 'POST'])
def support():
    return render_template('support.html')

@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    return render_template('prediction_form.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
