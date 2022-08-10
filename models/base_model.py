#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
from uuid import uuid
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import models
from datetime import datetime

if models.storage_t == 'db':
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """A base class for all hbnb models"""

     if models.storage_t == 'db':
        id = Column(String(60), primary_key=True, unique=True, nullable=False)
        created_at = Column(DateTime, default=datetime.utcnow(), 
                nullable=False)
        updated_at = Column(DateTime, default=datetime.utcnow(), 
                nullable=False)
    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if kwargs:
            for k, v in kwargs.items():
                if k != "__class__":
                    setattr(self, k, v)
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            if kwargs.get("id", None) is None:
                self.id = str(uuid4())
        else:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """save instance"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict"""
        dictionary = self.__dict__.copy()
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if '_sa_instance_state' in dictionary:
            del dictionary['_sa_instance_state']
        return dictionary

    def delete(self):
        """Delete instance"""
        from models import storage
        storage.delete(self)
