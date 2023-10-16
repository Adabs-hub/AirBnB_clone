#!/usr/bin/python3
"""BaseModel class Definition"""

import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    BaseModel class

    Desc: base class for all Airbnb project
    """

    def __init__(self):
        """Instance of all new models

        *kwargs (dict): key/value pairs of attributes
        """
        
        self.id = str(uuid4())
        timeform = "%Y-%m-%dT%H:%M:%S.%f"
        self.created_at = datetime.today()
        self.updated_at = datatime.taday()

        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self__dict__[k] = datatime.strptime(v, timeform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

        
    def save(self):
        """Update current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return BaseModel instance dictionary.

        Modifies updated_at time format to iso standard
        Modifies created_at time format to iso standard
        """
        modified_dict = self.__dict__.copy()
        modified_dict["updated_at"] = self.updated_at.isoformat()
        modified_dict["created_at"] = self.created_at.isoformat()
        modified_dict["__class__"] = self.__class__.__name__
        return modified_dict

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
