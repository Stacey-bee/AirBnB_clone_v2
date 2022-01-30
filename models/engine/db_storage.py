#!/usr/bin/python3

"""This module defines a class to manage database storage for hbnb clone"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import environ
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """This class manages storage of hbnb models in MySQL using SQLAlchemy"""
    __engine = None
    __session = None

    def __init__(self):
        """ constructor """
        user = environ.get('HBNB_MYSQL_USER')
        pwd = environ.get('HBNB_MYSQL_PWD')
        host = environ.get('HBNB_MYSQL_HOST')
        db = environ.get('HBNB_MYSQL_DB')
        env = environ.get('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                                      user, pwd, host, db), pool_pre_ping=True)
        if env == "test":
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """ query database based on the class specified """
        session = self.__session
        dct = {}

        if not cls:
            classes = [User, State, City, Amenity, Place, Review]
        else:
            if type(cls) == str:
                cls = eval(csl)
            classes = [cls]

        for curr_class in classes:
            query = session.query(curr_class).all()
            for rows in query:
                key = "{}.{}".format(type(rows).__name__, rows.id)
                dct[key] = rows

        return dct

    def new(self, obj):
        """ add object to current session """
        if obj:
            self.__session.add(obj)

    def save(self):
        """ commit changes of the current session """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete object on current session """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
            creates all tables in the database and
            creates the current database session
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        ''' closes session '''
        self.__session.close()
