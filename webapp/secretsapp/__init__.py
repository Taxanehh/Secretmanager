import secrets
from flask import Flask

import secretsapp.home

def create_app() -> Flask:
    app = Flask(__name__)
    app.config["SECRET_KEY"] = secrets.token_hex(64)
    app.register_blueprint(secretsapp.home.bp)

    return app
