#!/usr/bin/python3
import json

class Base():
    __nb_objects = 0

    @classmethod
    def save_to_file(cls, list_objs):
        filename = str(cls.__name__) + '.json'
        with open(filename, 'w+', encoding='utf-8') as f:
            f.seek(0)
            obj_list = []
            if len(list_objs) == 0:
                f.write(json.dumps(obj_list))
            else:
                for obj in list_objs:
                    obj_list += [obj.to_dictionary()]
                f.write(json.dumps(obj_list))

    def from_json_string(json_string):
        return json.loads(json_string)

    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
