"""Respositories for URL Shortener App."""

from db import Url, User

from .base import Repository


class UrlRepository(Repository[Url]):
    """URL Repository."""

    model = Url


class UserRepository(Repository[User]):
    """User Repository."""

    model = User
