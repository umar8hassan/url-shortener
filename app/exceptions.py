"""Custome Exceptions for URL Shortener."""


class ConfigError(Exception):
    """Exception class for missing Config."""

    def __init__(self, var: str) -> None:
        """Create instance of ConfigError class."""
        self.message = f"Missing config: {var}"
        super().__init__(self.message)
