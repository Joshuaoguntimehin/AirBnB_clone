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
        """Save storage dictionary to file."""
        with open(self.__file_path, 'w') as f:
            json.dump({obj_id: obj.to_dict() for obj_id, obj in self.__objects.items()}, f)

    def reload(self):
        """Load storage dictionary from file."""
        try:
            with open(self.__file_path, 'r') as f:
                obj_dict = json.load(f)
                for obj_id, obj_data in obj_dict.items():
                    self.__objects[obj_id] = BaseModel(**obj_data)
        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            pass  # If the file is empty or corrupted, ignore the error and start with an empty dictionary
