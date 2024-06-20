"""Flask APP for URL Shortener."""

from typing import Any

from flask import Flask
from flask_migrate import Migrate
from flask_swagger_ui import get_swaggerui_blueprint

from config import Config
from db import init_db

from .blueprints import swagger_bp, url_bp, user_bp


def register_blueprints(name: str, app: Flask) -> None:  # noqa: ARG001
    """Automatically register all blueprint packages."""


def swagger_init() -> Any:
    """Initialise swagger config."""
    swagger_url = "/docs"
    api_url = "/docs/specs.json"

    return get_swaggerui_blueprint(
        swagger_url, api_url, config={"app_name": "URL Shortener"}
    )


def create_app() -> Flask:
    """Create a URL Shortener App."""
    app = Flask(__name__)
    app.config.from_object(Config)

    db = init_db(app)

    Migrate(app, db)

    # register_blueprints()

    app.register_blueprint(swagger_init())
    app.register_blueprint(swagger_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(url_bp)

    return app
