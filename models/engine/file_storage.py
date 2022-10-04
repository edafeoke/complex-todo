#!/usr/bin/python3
'''file_storage module'''


class FileStorage:
    '''
    Serializes instances to a JSON file and deserializes
    JSON file to instances
    '''

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        '''
        Returns all objects
        '''
        return self.__objects

    def new(self, obj):
        '''
        sets in __objects the obj with
        key <obj class name>.id
        '''
        self.__object["{}.{}".format(obj.__class__,obj.id)] = obj

    def save(self):
        '''
        Serializes __objects to the JSON file
        '''
        pass
        # with open(self.__file_path, 'rw') as f:
        #     f.
