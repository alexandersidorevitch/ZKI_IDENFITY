import hashlib


class Encode:
    @staticmethod
    def encode(string: str):
        return hashlib.sha256(string.encode()).hexdigest()
