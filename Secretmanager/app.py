# Paul Stokreef
# Secretmanager Assignment
# To be implemented: double username check, login mechanism, encryption / decryption

# Standard flask import for rendering the pages (templates)
from flask import Flask, render_template
# Os import to make sure .csv file works on every OS
import os

app = Flask(__name__, template_folder='pages', static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)