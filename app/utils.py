"""Utils for URL Shortener App."""

import random
import string

from .constants import DEFAULT_CODE_LENGTH


def get_code(length: int = DEFAULT_CODE_LENGTH) -> str:
    """Shorten the given url."""
    return "".join(random.choices(string.ascii_lowercase + string.digits, k=length))
