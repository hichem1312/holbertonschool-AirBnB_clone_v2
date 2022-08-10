#!/usr/bin/python3
"""Mysql Storage"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """manaing the storage with mysql."""

    __engine = None
    __session = None

    def __init__(self):
        """initialize engine and session"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            from models.base_model import Base
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """return a dictionary"""
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        obj = {}
        if cls:
            for i in self.__session.query(cls).all():
                obj[i.__class__.__name__ + '.' + i.id] = i
            return obj
        else:
            for i in self.__session.query(User, State, City,
                                            Place, Amenity, Review).all():
                obj[i.__class__.__name__ + '.' + i.id] = i
            return obj

    def new(self, obj):
        """add object"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create tables """
        from models.base_model import Base
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def close(self):
        """Close session"""
        self.__session.close()
