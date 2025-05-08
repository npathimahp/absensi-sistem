from flask import Flask
import firebase_admin
from firebase_admin import credentials
from firebase_admin import initialize_app as firebase_initialize_app
import json

from . import config
from .utils import format_datetime


def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    app.secret_key = config.SECRET_KEY

    # Register custom Jinja filter
    app.jinja_env.filters["format_datetime"] = format_datetime

    # Initialize Firebase only if not already initialized
    if not firebase_admin._apps:
        try:
            cred_dict = json.loads(config.FIREBASE_CREDENTIALS_JSON)
            cred = credentials.Certificate(cred_dict)

            firebase_initialize_app(
                cred,
                {
                    "databaseURL": config.DATABASE_URL,
                    "storageBucket": config.STORAGE_BUCKET,
                },
            )
        except Exception as e:
            raise RuntimeError(f"Failed to initialize Firebase: {e}")

    # Register routes blueprint
    from . import routes
    app.register_blueprint(routes.bp)

    return app
