"""Base module for Base Repository and UoW."""

from functools import cached_property
from types import SimpleNamespace
from typing import Callable, Dict, Generic, List, TypeVar, Union

from sqlalchemy.orm import Session

from app.repositories.abstract import AbstractRepository, AbstractUnitOfWork
from db import Base

ModelType = TypeVar("ModelType", bound=Base)


class Repository(AbstractRepository, Generic[ModelType]):
    """Base Repository for Models."""

    model: ModelType

    def __init__(self, session: Session):
        """Create instance of base Repository."""
        self.session = session

    def filter_by(self, **kwargs) -> List[ModelType]:
        """Apply filters by key value pairs."""
        return self.session.query(self.model).filter_by(**kwargs)

    def filter(self, *criterion) -> List[ModelType]:
        """Apply sqlalchemy filter maps."""
        return self.session.query(self.model).filter(*criterion)

    def save(self, model: ModelType):
        """Add model object to DB."""
        self.session.add(model)

    def get(self, id_: int) -> ModelType:
        """Get single entity by id."""
        return self.session.query(self.model).get(id_)

    def all(self) -> List[ModelType]:
        """Get all data from DB."""
        return self.session.query(self.model)


class UnitOfWork(AbstractUnitOfWork):
    """Base Unit of Work for Respository."""

    def __init__(
        self,
        session: Union[Callable[[], Session], Session],
        **kwargs: Dict[str, Repository],
    ):
        """Create instance of UoW."""
        self._session = session
        self._repository_config = kwargs

    @cached_property
    def session(self):
        """Cache session aqcuired from session factory."""
        return self._session() if callable(self._session) else self._session

    def __enter__(self) -> AbstractUnitOfWork:
        """Entry method for the UoW."""
        repositories = {
            name: repository(self.session)
            for name, repository in self._repository_config.items()
        }
        self.repositories = SimpleNamespace(**repositories)
        return super().__enter__()

    def __exit__(self, *args):
        """Exit method for the UoW."""
        self.session.close()

    def commit(self):
        """Commit transaction in UoW."""
        self.session.commit()

    def rollback(self):
        """Rollback transaction in UoW."""
        self.session.rollback()
