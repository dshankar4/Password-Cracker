from flask import Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
from flask import Flask, render_template, url_for, flash, redirect, request
import feedparser
from dateutil import parser as date_parser
from database import addUser, validateUser
@app.route('/', methods=['POST', 'GET'])
def index(): 
    return redirect(url_for('login'))
@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST': 
        username = request.form['username']
        password = request.form['password']
        user=addUser(username,password) 
        return render_template('login_s.html')
    return render_template('login.html', title='Register')
@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST': 
        username = request.form['username']
        password = request.form['password']
        user=validateUser(username,password)
        global admin
        if user == -1:
            return render_template('login.html', title='Login')
        elif user == 1:
            admin=1
            return render_template('login_s.html')
        else:
            admin=0
            return render_template('login_s.html')
    return render_template('login.html', title='Login')
if __name__ == '__main__':
    app.run()

