#!/usr/bin/python3
"""Model Base module doc"""
from uuid import uuid4
from datetime import datetime


class BaseModel():
    """class BaseModel doc"""

    def __init__(self, id=None):
        """constructor method doc"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """str doc"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """save doc"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """to dict doc"""
        my_dict = self.__dict__
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = self.created_at.isoformat("\
#", "microseconds")
        my_dict["updated_at"] = self.updated_at.isoformat("\
#", "microseconds")
        return my_dict