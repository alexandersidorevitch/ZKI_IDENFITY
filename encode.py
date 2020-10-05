import hashlib
import uuid


class Encode:
    @staticmethod
    def encode(string: str):
        salt = uuid.uuid4().hex
        return hashlib.sha256(salt.encode() + string.encode()).hexdigest() + ':' + salt

    @staticmethod
    def check_password(hashed_password, user_password):
        password, salt = hashed_password.split(':')
        return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()
