"""Blueprint for the URL module."""

from flask import Blueprint, jsonify, redirect, request

from db import Url, session_factory

from ..repositories import UnitOfWork, UrlRepository
from ..utils import get_code

url_bp = Blueprint("urls", __name__, url_prefix="/url")


@url_bp.post("/add")
def add_url():
    """Add a new url."""
    data = request.json

    original_url = Url(**data)

    with UnitOfWork(session=session_factory, url_repository=UrlRepository) as uow:
        url = uow.repositories.url_repository.filter_by(url=original_url.url).first()
        if not url:
            url = original_url
            url.code = get_code()
            uow.repositories.url_repository.save(url)

        uow.commit()

        return jsonify(url.to_dict())


@url_bp.get("/<code>")
def redirect_url(code):
    """Redirect to original URL."""
    with UnitOfWork(session=session_factory, url_repository=UrlRepository) as uow:
        url = uow.repositories.url_repository.filter_by(code=code).first()
        if url:
            url.clicks += 1
            uow.commit()
        else:
            return "URL not registered with us.", 404

        return redirect(url.url)
