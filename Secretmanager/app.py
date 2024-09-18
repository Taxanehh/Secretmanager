# Paul Stokreef
# Secretmanager Assignment
# To be implemented: check for blur removal vulnerability, 
# XSS Test, 2FA, HTTPS, better UI? 
# maybe footer fix, looks nice now though,

# Standard flask import for rendering the pages (templates)
# Flask import for requesting data from forms and submitting them to files
# Flask import for flashing warnings / messages
# Flask import for session to prevent double user logins under same name
# Flask import for redirecting login to dashboard
# Flask import for finding redirects (because for some reason that's how it works)
from flask import Flask, render_template, request, flash, session, redirect, url_for
# Bcrypt for session encryption & user encryption
from flask_bcrypt import Bcrypt
# Fernet for encrypting and decrypting secrets as an extra layer of security
from cryptography.fernet import Fernet
# Datetime import to get todays date and time for login time mechanism
from datetime import datetime
# Os import to make sure .csv file works on every OS
import os
# CSV reading utilities
import csv

app = Flask(__name__, template_folder='pages', static_folder='static')
bcrypt = Bcrypt(app)
app.secret_key = 'paulus'

# Secret key for encrypting and decrypting passwords (replace with your own saved key)
fernet_key = b'cVpK1oJHq5E4cK_pltia43Vr1GekwO4dA_UlLDK-xgM='
cipher = Fernet(fernet_key)

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
            writer.writerow([name, username, password_hash, ""]) # Creates 3 rows in our csv: the real name, username and hashed password
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

# Make sure the login is valid by scanning the file
def validate_login(username, password):
    try:
        rows = []
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(USER_DATA_FILE, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[1] == username: # Scrapped row length check, since more and more get added
                    if bcrypt.check_password_hash(row[2], password):
                        # Store previous login time
                        last_login_time = row[3] if row[3] else None

                        # Update last_login_time to current time
                        row[3] = current_time
                        rows.append(row)

                        # Return success with the last login time
                        return True, last_login_time
                rows.append(row)
    except FileNotFoundError:
        print("User data file not found.")
    except Exception as e:
        print(f"Error reading user data: {e}")
    return False

# Save the updated rows with the new login time
def update_user_last_login(rows):
    try:
        with open(USER_DATA_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
    except Exception as e:
        print(f"Error updating user data: {e}")

# Encrypt password before saving
def encrypt_password(plain_password):
    return cipher.encrypt(plain_password.encode()).decode()

# Decrypt password for viewing
def decrypt_password(encrypted_password):
    return cipher.decrypt(encrypted_password.encode()).decode()

# Save the password along with the associated username
def save_password(username, site, account_username, account_password, custom_code):
    encrypted_password = encrypt_password(account_password)
    try:
        with open(PASSWORD_DATA_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([username, site, account_username, encrypted_password, custom_code])
    except Exception as e:
        print(f"Error saving password: {e}")

# Load passwords filtered by the logged-in username
def load_passwords(username):
    passwords = []
    try:
        with open(PASSWORD_DATA_FILE, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                # Check if it's the correct file
                if len(row) < 5: # Made extra row for unique ~~UUID~~ Custom code
                    continue
                if row[0] == username:  # Only load passwords for the logged-in user
                    passwords.append([row[1], row[2], row[3], row[4]])  # Store encrypted passwords
    except FileNotFoundError:
        print("Password data file not found.")
    except Exception as e:
        print(f"Error reading password data: {e}")
    return passwords

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
        
        # Validate that the username and password do not contain spaces
        if ' ' in username:
            flash('Username cannot contain spaces.')
            return render_template('register.html')

        if ' ' in password:
            flash('Password cannot contain spaces.')
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

        is_valid, last_login_time = validate_login(username, password)
        if is_valid and username and password and validate_login(username, password):
            session['username'] = username
            session['last_login_time'] = last_login_time  # Store the last login time in session
            update_user_last_login()
            return redirect(url_for('dashboard'))  # Redirect correctly to the dashboard
        else:
            flash('Invalid login credentials.') # No invalid password / username! for security reasons :)

    return render_template('login.html')  # This should render the login page

@app.route('/dashboard', methods=['GET']) # Scrapped POST; scrapped UUID
def dashboard():
    username = session.get('username')
    if not username:
        return redirect(url_for('login'))  # Ensure only logged-in users can access the dashboard
    
    last_login_time = session.get('last_login_time')

    if last_login_time:
        # Calculate the time difference between now and the last login
        last_login_dt = datetime.strptime(last_login_time, '%Y-%m-%d %H:%M:%S')
        current_time = datetime.now()
        time_diff = current_time - last_login_dt

        days = time_diff.days
        hours, remainder = divmod(time_diff.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        if days > 0:
            time_since_last_login = f"{days} days, {hours} hours, and {minutes} minutes ago"
        elif hours > 0:
            time_since_last_login = f"{hours} hours and {minutes} minutes ago"
        else:
            time_since_last_login = f"{minutes} minutes ago"
    else:
        time_since_last_login = "Welcome, you've logged in for the first time!"

    # Pagination logic
    page = request.args.get('page', 1, type=int)  # Get the page number from the URL, default is page 1
    per_page = 10  # Number of passwords to display per page
    passwords = load_passwords(username)

    # Small mechanism to handle searching by unique code :)
    if request.method == 'POST':
        search_code = request.form.get('search_code')
        if search_code:
            passwords = [pw for pw in passwords if pw[3] == search_code]  # Filter by the unique code

    # Calculate total pages and get the slice of passwords for the current page
    total_pages = (len(passwords) + per_page - 1) // per_page  # Ceiling division to calculate total pages
    passwords_on_page = passwords[(page - 1) * per_page: page * per_page]  # Slice the list for current page

    return render_template(
        'dashboard.html', 
        passwords=passwords_on_page, 
        page=page, 
        total_pages=total_pages,
        time_since_last_login=time_since_last_login
    )

# Separate route to handle adding passwords without interfering with viewing
@app.route('/add_password', methods=['POST'])
def add_password():
    username = session.get('username')
    if not username:
        return redirect(url_for('login'))  # Ensure only logged-in users can add passwords

    # Process the form submission to add a new password
    site = request.form.get('site')
    account_username = request.form.get('account_username')
    account_password = request.form.get('account_password')
    custom_code = request.form.get('custom_code')

    if ' ' in account_username:
            flash('Username cannot contain spaces.')
            return redirect(url_for('dashboard'))

    if ' ' in account_password:
        flash('Password cannot contain spaces.')
        return redirect(url_for('dashboard'))
    
    if ' ' in custom_code:
        flash('Code cannot contain spaces.')
        return redirect(url_for('dashboard'))

    # STRUCTURE OF PASSWORD.CSV!!!
    save_password(username, site, account_username, account_password, custom_code)
    flash('Password saved successfully!')
    return redirect(url_for('dashboard'))

# New API route to handle decrypting password via AJAX
# This is to prevent the URL from switching to dashboard/1 , ../2 etc
# (Huge thanks to my little brother for the tip!)
@app.route('/api/decrypt_password', methods=['POST'])
def api_decrypt_password():
    username = session.get('username')
    if not username:
        return {'error': 'Not logged in'}, 401

    index = request.json.get('index')
    passwords = load_passwords(username)

    # gather the password and decrypt it, ready to show it
    if 0 <= index < len(passwords):
        encrypted_password = passwords[index][2]
        decrypted_password = decrypt_password(encrypted_password)
        # 200 is the net code for continue
        return {'password': decrypted_password}, 200

    return {'error': 'Invalid password index'}, 400

@app.route('/edit_password/<int:index>', methods=['POST'])
def edit_password(index):
    # As you see, each command checks for session legitimacy
    username = session.get('username')
    if not username:
        return redirect(url_for('login'))

    # Gather the username and password from the form
    site = request.form.get('site')
    account_username = request.form.get('account_username')
    account_password = request.form.get('account_password')
    custom_code = request.form.get('custom_code')

    if ' ' in account_username:
        flash('Edited Username cannot contain spaces.')
        return redirect(url_for('dashboard'))

    if ' ' in account_password:
        flash('Edited Password cannot contain spaces.')
        return redirect(url_for('dashboard'))
    
    if ' ' in custom_code:
        flash('Edited Code cannot contain spaces.')
        return redirect(url_for('dashboard'))

    # Encrypt the new password
    encrypted_password = encrypt_password(account_password)

    # Read all passwords and update the specific one
    passwords = load_passwords(username)

    if 0 <= index < len(passwords):
        passwords[index] = [site, account_username, encrypted_password, custom_code]

        # Save the updated password list back to the CSV file
        try:
            with open(PASSWORD_DATA_FILE, mode='w', newline='') as file:
                writer = csv.writer(file)
                for row in passwords:
                    writer.writerow([username] + row)  # Save username with each password
        except Exception as e:
            print(f"Error updating password: {e}")

    flash('Password updated successfully!')
    return redirect(url_for('dashboard'))

# New route to handle deleting a password
@app.route('/delete_password/<int:index>', methods=['POST'])
def delete_password(index):
    username = session.get('username')
    if not username:
        return redirect(url_for('login'))

    passwords = load_passwords(username)

    if 0 <= index < len(passwords):
        passwords.pop(index)
        # Overwrite the CSV file with updated passwords
        with open(PASSWORD_DATA_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            for pw in passwords:
                writer.writerow([username] + pw)

        flash('Password deleted successfully!')
    else:
        flash('Invalid password index.')

    return redirect(url_for('dashboard'))

@app.route('/logout')
def logout():
    # If a user tries to put /logout in the url, check for session
    if 'username' in session:
        session.pop('username', None)
        flash('Logged out succesfully!')
        return redirect(url_for('index'))
    else:
        flash('You are not logged in')
        return redirect(url_for('index'))

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)