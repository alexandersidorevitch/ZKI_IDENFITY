import json


class Load:
    @staticmethod
    def load_from_file(file):
        with open(file, 'r') as f:
            return json.load(f)

    @staticmethod
    def load_to_file(file, data):
        with open(file, 'w') as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def return_el_with_login(data, login):
        for el in data:
            if el.get('login', None) == login:
                return el
        else:
            return None
