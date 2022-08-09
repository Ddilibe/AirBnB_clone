#!/usr/bin/python3
"""
    Module used to convert a dictionary to a JSON string
"""
import json


class FileStorage:
    """
    Class That serializes instances to a JSON file and deserializes JSON
    file to the instances

    Private Instances
        __file_path: Contains the string path the json file
        __objects: Dictionary that will store all objects by class name
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Public Instance that returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ Public Instance Method that adds the atribute to the dictionary """
        name = str(obj.__class__.__name__) + '.' + str(obj.id)
        FileStorage.__objects[name] = obj

    def save(self):
        """
        Public Instance Method that serializes __objects to the JSON path
        """
        new_dictionary = {}
        for keys, value in FileStorage.__objects.items():
            new_dictionary[keys] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as w:
            json.dump(new_dictionary, w)

    def reload(self):
        """
        Public Instance to deserialize the JSON FILE to __object
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        major_class = {
                "User": User,
                "BaseModel": BaseModel,
                "Place": Place,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Review": Review
                }
        try:
            with open(self.__file_path, 'r') as done:
                dictionary = json.load(done)
                for keys, value in dictionary.items():
                    semi_key = str(keys).split('.')[0]
                    self.new(major_class[semi_key](**value))
        except Exception:
            pass
