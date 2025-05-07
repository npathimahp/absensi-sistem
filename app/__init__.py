from flask import Flask
import firebase_admin
from firebase_admin import credentials
import json

from . import config
from .utils import format_datetime


def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    app.secret_key = config.SECRET_KEY
    app.jinja_env.filters["format_datetime"] = format_datetime

    # Firebase setup from JSON string (for Railway)
    cred_dict = json.loads(config.FIREBASE_CREDENTIALS_JSON)
    cred = credentials.Certificate(cred_dict)

    firebase_admin.initialize_app(
        cred,
        {
            "databaseURL": config.DATABASE_URL,
            "storageBucket": config.STORAGE_BUCKET,
        },
    )

    # Import and register the blueprint
    from . import routes
    app.register_blueprint(routes.bp)

    return app
