#!/usr/bin/python3
"""a basemodel that defines all common attrs/models for other classes"""

import uuid
from datetime import datetime
import models


class BaseModel():
    """this is the class that defines common stuff"""

    def __init__(self, *args, **kwargs):
        """ a constructor instance that prefarably uses of kwargs if !empty"""

        if kwargs:
            for k, v in kwargs.items():
                if key == '__class__':
                    continue
                elif key == "created_at" or key == "updated_at":
                    time = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, time)
                else:
                    setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

        def __str__(self):
            """this returns a string representation of the isinstance"""
            return ("[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                          self.__dict__))

        def save(self):
            """this updates and saves the public instance attribute
            updated_at with the latest datetime"""
            self.updated_at = datetime.now()
            models.storage.save()

        def to_dict(self):
            """returns a serialized dictionary containing
            the keys / value of the instance"""
            dict_rep = self.__dict__.copy()
            dict_rep.update({'__class__': self.__class__.__name__})
            dict_rep.update({'created_at': self.created_at.isoformat()})
            dict_rep.update({'updated_at': self.updated_at.isoformat()})
            return (dict_rep)
