"""Blueprint for the Users module."""

from flask import Blueprint, jsonify, request

from db import User, session_factory

from ..repositories import UnitOfWork, UserRepository

user_bp = Blueprint("users", __name__, url_prefix="/user")


@user_bp.post("/add")
def add_user():
    """Create a new user."""
    data = request.json

    user = User(**data)

    with UnitOfWork(session=session_factory, user_repository=UserRepository) as uow:
        uow.repositories.user_repository.save(user)

        uow.commit()

        return jsonify(user.to_dict())
