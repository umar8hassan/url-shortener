"""Blueprint for the Swagger module."""

from flask import Blueprint, send_file

swagger_bp = Blueprint("swagger", __name__, url_prefix="/docs")


@swagger_bp.get("/specs.json")
def swagger_specs():
    """Get swagger specs file."""
    return send_file("blueprints/swagger.json")
