"""Models for URL Shortener App."""

import datetime
from functools import cached_property

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import DeclarativeBase, backref, relationship


class Base(DeclarativeBase):
    """Base Class for Model declarations."""

    def to_dict(self):
        """Convert Model object to dict."""
        return {field.name: getattr(self, field.name) for field in self.__table__.c}


class User(Base):
    """Model for Users."""

    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(32), nullable=False)
    last_name = Column(String(32), nullable=False)
    email = Column(String(64), nullable=False, unique=True)
    created_at = Column(DateTime(timezone=True), default=datetime.datetime.now)
    updated_at = Column(DateTime(timezone=True), default=datetime.datetime.now)

    @cached_property
    def name(self):
        """User Name property."""
        return self.first_name + " " + self.last_name

    def __repr__(self):
        """Representation of User Model."""
        return f"<User {self.name!r}>"


class Url(Base):
    """Model for URLs."""

    __tablename__ = "url"

    id = Column(Integer, primary_key=True)
    url = Column(String(500), nullable=False)
    code = Column(String(20), unique=True, nullable=False)
    owner_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    owner = relationship("User", backref=backref("urls", lazy=True))
    is_private = Column(Boolean, default=False)
    clicks = Column(Integer, default=int())
    created_at = Column(DateTime(timezone=True), default=datetime.datetime.now)
    updated_at = Column(DateTime(timezone=True), default=datetime.datetime.now)
