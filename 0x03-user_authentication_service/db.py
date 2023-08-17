#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

from user import Base, User
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """returns user object"""
        try:
            new_user = User(email=email, hashed_password=hashed_password)
            self._session.add(new_user)
            self._session.commit()
        except Exception:
            self._session.rollback()
            self._session = None
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """returns the first row found in the users
        table as filtered by the method’s input arguments"""
        query_dict = {}
        for key, value in kwargs.items():
            if hasattr(User, key):
                query_dict[key] = kwargs[key]
            else:
                raise InvalidRequestError()
        result = self.__session.query(User).filter_by(**query_dict).first()
        if result is None:
            raise NoResultFound()
        return result

    def update_user(self, user_id: int, **kwargs) -> None:
        """Updates a user based on a given id.
        """
        user = self.find_user_by(id=user_id)
        if user is None:
            return
        update_dict = {}
        for key, value in kwargs.items():
            if hasattr(User, key):
                update_dict[key] = kwargs[key]
            else:
                raise ValueError()
        self._session.query(User).filter(User.id == user_id).update(
            update_dict,
            synchronize_session=False,
        )
        self._session.commit()
