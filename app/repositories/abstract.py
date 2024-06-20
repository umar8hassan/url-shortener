"""Abstract Repository and UoW."""

import abc
from collections.abc import Iterable
from types import SimpleNamespace
from typing import Any


class AbstractRepository(abc.ABC):
    """Abstract Repository class."""

    @abc.abstractmethod
    def all(self, model: Any) -> Any:
        """Abstract Repository method to get all objects."""
        raise NotImplementedError

    @abc.abstractmethod
    def filter(self, **kwargs: Any) -> Iterable[Any]:
        """Abstract Repository method to apply filters."""
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, _id: Any):
        """Abstract Repository method to get single object by id."""
        raise NotImplementedError

    @abc.abstractmethod
    def save(self, model: Any):
        """Abstract Repository method to add model instance to DB."""
        raise NotImplementedError


class AbstractUnitOfWork(abc.ABC):
    """Context Manager to work with abstract Repository."""

    repositories: SimpleNamespace

    def __enter__(self) -> "AbstractUnitOfWork":
        """Enter method for UoW context managers."""
        return self

    def __exit__(self, *args):
        """Exit method for UoW context manager."""

    @abc.abstractmethod
    def commit(self):
        """Commit method for UoW for repository."""
        raise NotImplementedError

    @abc.abstractmethod
    def rollback(self):
        """Rollback method for UoW for repository."""
        raise NotImplementedError
