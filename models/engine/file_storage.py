import json
import os

class FileStorage:
    __file_path = "file.json"
    __object = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__object

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = f"{obj.__class__.__name__}"

    def save(self):
        """ Serialize an object to a file"""
        with open(self.__file_path, 'w') as file:
            json.dump(self.__object, file, default=self._serialize_helper)

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

