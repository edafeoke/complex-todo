#!/usr/bin/python3
'''base_model module'''

from datetime import datetime
from uuid import uuid4


class BaseModel:
    '''A class that defines all common attributes/methods for other classes'''

    def __init__(self) -> None:
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return '[{}] ({}) <{}>'.format(self.__class__.__name__, self.id, self.__dict__)

    def save(self) -> None:
        '''updates the public instance attribute updated_at with the current datetime'''
        self.updated_at = datetime.now()

    def to_dict(self) -> dict:
        '''
        Returns a dictionary containing all keys/values of __dict__ of the
        instance
        '''
        obj = {}

        for k, v in self.__dict__.items():
            if k == "created_at" or k == "updated_at":
                v = v.isoformat()
            obj[k] = v
        obj['__class__'] = self.__class__.__name__
        return obj
