# Flask Web Application

## Overview

This project is a **Flask** web application designed to manage secrets with user authentication and two-factor authentication (2FA). The application allows users to securely store and manage their credentials or secrets using Flask and an integrated dashboard. The app is built with a clean front-end and uses **Nginx** as a reverse proxy when deployed on a Linux server.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
  - [System Requirements](#system-requirements)
  - [Steps to Install](#steps-to-install)
- [License](#license)

## Features

- **User Authentication**: Secure user registration and login with password hashing (via Flask-SQLAlchemy).
- **Two-Factor Authentication (2FA)**: Adds an additional layer of security post-login.
- **Secret Management**: Store, edit, delete, and view secrets/credentials in a secure dashboard.
- **Pagination**: Secrets can be paginated for easier navigation.
- **Flash Messaging**: Informational and error messages displayed using Flask’s flash messaging system.
- **Session Management**: User sessions are managed securely.

## Project Structure

```bash
├── app.py               # Main Flask application
├── static/              # Static files (CSS, JavaScript, images)
│   ├── styles/
│   │   └── globals.css  # Main stylesheet
│   └── public/
│       └── logo.ico     # Site logo
├── templates/           # HTML templates for Jinja2 rendering
│   ├── dashboard.html   # User dashboard page
│   ├── login.html       # Login page
│   ├── register.html    # Registration page
│   └── 2fa.html         # Two-factor authentication page
├── .env                 # Environment variables (Flask secret keys, DB URI)
├── README.md            # This README file
└── requirements.txt     # Python dependencies for the project
```

## Installation

### System Requirements

- **Python 3.8+**
- **Flask 2.0+**
- **Nginx** (for deployment)
- **pip** (Python package manager)

### Steps to Install

- Start nginx

```bash
start nginx
```

- Clone the repository

```bash
git clone https://github.com/your-username/your-flask-app.git
cd your-flask-app
```

- Install Dependencies

```bash
pip install -r requirements.txt
```

- Set environment variables by changing the app.secret_key & fernet_key

- Run the following command to initialize the application:

```bash
flask run
```

- Open your web browser and go to:

```bash
https://127.0.0.1:5000 or http://localhost
```

- This project is licensed under the GNU General Public License v3.0 License.

