# Paul Stokreef
# Secretmanager Assignment
# To be implemented: double username check, login mechanism, encryption / decryption

# Standard flask import for rendering the pages (templates)
# Flask import for requesting data from forms and submitting them to files
# Flask import for flashing warnings / messages
# Flask import for session to prevent double user logins under same name
# Flask import for redirecting login to dashboard
# Flask import for finding redirects (because for some reason that's how it works)
from flask import Flask, render_template, request, flash, session, redirect, url_for
# Bcrypt for session encryption & user encryption
from flask_bcrypt import Bcrypt
# Os import to make sure .csv file works on every OS
import os
# CSV reading utilities
import csv

app = Flask(__name__, template_folder='pages', static_folder='static')
bcrypt = Bcrypt(app)
app.secret_key = 'paulus'

# Seperate .CSV files for user data and secrets data
USER_DATA_FILE = os.path.join(os.path.dirname(__file__), 'users.csv')
PASSWORD_DATA_FILE = os.path.join(os.path.dirname(__file__), 'passwords.csv')

# Main page: say the url has nothing after the /, get directed to index.html
@app.route('/')
def index():
    return render_template('index.html')

# Save new user to CSV
def save_user(name, username, password_hash):
    try:
        with open(USER_DATA_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, username, password_hash]) # Creates 3 rows in our csv: the real name, username and hashed password
    except Exception as e:
        print(f"Error saving user: {e}")

# Check if the username already exists
def is_username_taken(username):
    try:
        with open(USER_DATA_FILE, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[1] == username:  # Check if the username matches
                    return True
    except FileNotFoundError:
        pass
    return False

def validate_login(username, password):
    try:
        with open(USER_DATA_FILE, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) < 3:  # Ensure the row has at least 3 columns
                    continue
                if row[1] == username:
                    if bcrypt.check_password_hash(row[2], password):
                        return True
    except FileNotFoundError:
        print("User data file not found.")
    except Exception as e:
        print(f"Error reading user data: {e}")
    return False

# Register mechanism
@app.route('/register', methods=['GET', 'POST'])
def register():
    # Gather the info put in the form
    if request.method == 'POST':
        name = request.form.get('name')
        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        # Check if the username is already taken
        if is_username_taken(username):
            flash('Username is already taken. Please choose a different one.')
            return render_template('register.html')

        if not username:
            flash('Username is required.')
        elif password != confirm_password:
            flash('Passwords do not match.')
        else:
            password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
            save_user(name, username, password_hash)
            flash('Registration complete! Please log in.')
    
    return render_template('register.html')

# Login mechanism
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username and password and validate_login(username, password):
            session['username'] = username
            return redirect(url_for('dashboard'))  # Redirect correctly to the dashboard
        else:
            flash('Invalid login credentials.')

    return render_template('login.html')  # This should render the login page

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)