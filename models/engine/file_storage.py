#!/usr/bin/python3
import datetime
import json
import os

class FileStorage:
    """Class to handle storage of objects to and from a JSON file."""
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects
    
    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def _serialize_helper(self, obj):
        """ Helper function for serializing non-serializable objects. """
        # Implement custom serialization logic here
        pass

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, f)

    @staticmethod
    def _deserialize_helper(d):
        """Custom deserialization logic."""
        # Implement your custom deserialization logic here.
        # For example, you may need to convert dictionaries back to object instances.
        return d
    
    def reload(self):
        """Deserializes the JSON file to __objects, if the file exists."""
        if os.path.exists(self.__file_path):
            try:
                with open(self.__file_path, 'r', encoding="utf-8") as file:
                    loaded_objects = json.load(file, object_hook=FileStorage._deserialize_helper)
                    self.__objects = loaded_objects
            except (json.JSONDecodeError, IOError) as e:
                print(f"Error loading from {self.__file_path}: {e}")

