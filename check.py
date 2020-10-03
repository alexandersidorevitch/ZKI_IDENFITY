from functools import reduce


class Check:
    def __init__(self):
        import string
        self.letters = tuple(el for el in string.ascii_letters + string.punctuation) + tuple(
            map(lambda el: str(el), range(10)))
        self.forbidden_characters = tuple(el for el in string.punctuation + ' ')
        self.weights = tuple(50 for _ in range(52)) + tuple(10 for _ in range(32)) + tuple(40 for _ in range(10))

    def is_suitable_string(self, string: str) -> bool:
        return not string.startswith(self.forbidden_characters)

    def is_suitable_raise(self, string: str) -> str:
        if self.is_suitable_string(string):
            return string
        else:
            raise ValueError

    def random_password(self):
        from random import choices, randint
        password = '.'
        while not self.is_suitable_string(password):
            password = reduce(lambda x, y: f'{x}{y}', choices(self.letters, k=randint(7, 20),
                                                              weights=self.weights))
        return password
