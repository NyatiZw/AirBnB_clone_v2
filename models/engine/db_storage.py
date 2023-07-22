#!/usr/bin/python3
"""Defines the dbstorage engine"""
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker


class DBStorage:
    """Represents a database storage engine.
    Attributes:
        __engine (sqlalchemy.Engine): The working SQLAlchemy engine.
        __session (sqlalchemy.Session): The working SQLAlchemy session.
    """

    __engine = None
    __session = None

    def __init__(self):
        """Initialize a ne Database instance."""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                     format(getenv("HBNB_MYSQL_USER"),
                                            getenv("HBNB_MYSQL_PWD"),
                                            getenv("HBNB_MYSQL_HOST"),
                                            getenv("HBNB_MYSQL_DB")),
                                     pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Querring the current database session"""
        if cls is None:
            obj = self.__session.query(State).all()
            obj.extend(self.__session.query(City).all()
            obj.extend(self.__session.query(User).all()
            obj.extend(self.__session.query(Place).all()
            obj.extend(self.__session.query(Review).all()
            obj.extend(self.__session.query(Amenity).all()
        else:
            if type(cls) == str:
                cls = eval(cls)
            obj = self.__session.query(cls)
        return {"{}.{}".format(type(o).__name__, o.id): o for o in obj}

    def new(self, obj):
        """Adds new object to the current db session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes to the db session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes obj instance ffrom current db session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):$
        """Create all tables in the db and init a new session"""
        Base.metadata.create_all(self.__engine)
        session_f = sessionmaker(bind=self.__engine,
                                 expire_on_commit=False)
        Session = scoped_session(session_f)
        self.__session = Session()

    def close(self):
        """Close the working SQLAlchemy session."""
        self.__session.close()