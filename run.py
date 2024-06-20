"""Start a Flask App for URL Shortener."""

import logging
import sys

from app import create_app
from app.exceptions import ConfigError
from config import Config

try:
    app = create_app()

    log_handler = logging.StreamHandler()
    log_handler.setFormatter(
        logging.Formatter(
            "%(asctime)s %(levelname)s [%(filename)s:%(lineno)d] %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
    )
    log_handler.setLevel(getattr(logging, Config.LOG_LEVEL))
    app.logger.addHandler(log_handler)
    app.logger.setLevel(getattr(logging, Config.LOG_LEVEL))
    app.logger.info("Started URL Shortener app...")

except ConfigError as error:
    print(f"Error: {error.message}")  # noqa: T201
    sys.exit(1)

if __name__ == "__main__":
    app.run()
