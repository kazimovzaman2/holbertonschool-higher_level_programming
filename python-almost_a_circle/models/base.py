#!/usr/bin/python3
"""Base class for all other classes in the model package."""
import json


class Base:
    """Represents the Base class.

    Base class for all other classes in the model package.

    Attributes:
        __nb_objects (int): The number of objects created.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes an instance of the Base class.

        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert a list of dictionaries to a JSON string representation.

        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Deserialize a JSON string representation into a Python object.

        Args:
            json_string (str): The JSON string to be deserialized.
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves a list of objects to a JSON file.

        Args:
            cls (class): The class of the objects.
            list_objs (list): The list of objects to be saved.
        """
        if list_objs is None:
            list_dictionary = []
        else:
            list_dictionary = [obj.to_dictionary() for obj in list_objs]

        filename = "{}.json".format(cls.__name__)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_dictionary))

    @classmethod
    def create(cls, **dictionary):
        """Creates a new instance of the class based on the given dictionary.

        Args:
            dictionary (dict): A dictionary containing the attributes of the instance.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 2)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = "{}.json".format(cls.__name__)

        try:
            with open(filename, "r", encoding="utf-8") as f:
                json_string = f.read()
                list_dicts = cls.from_json_string(json_string)
                instances = []
                for d in list_dicts:
                    instance = cls.create(**d)
                    instances.append(instance)
                return instances
        except IOError:
            return []
