"""DB module for URL Shortener App."""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from config import Config
from db.models import Base, Url, User

engine_factory = create_engine(Config.SQLALCHEMY_DATABASE_URI)

session_factory = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine_factory)
)

Base.metadata.bind = engine_factory
Base.query = session_factory.query_property()


def init_db(app: Flask) -> SQLAlchemy:
    """Initialise DB for App."""
    db = SQLAlchemy(model_class=Base)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    return db
