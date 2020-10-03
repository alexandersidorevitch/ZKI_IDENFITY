import hashlib

from hashids import Hashids

from check import Check
from load_from_json import Load


class Main(Load, Check):
    def __init__(self):
        super().__init__()
        main_file = 'file.json'
        hashids = Hashids(salt='1')

        while True:
            try:
                all_data = self.load_from_file(main_file)
            except FileNotFoundError:
                all_data = []
            print('1. Войти')
            print('2. Зарегистрироваться')
            print('3. Восстановить пароль')

            inputted = input('Выберите пункт: ')
            if inputted == '1':
                login = input('Введите логин: ')
                if not self.is_suitable_string(login):
                    print('Нельзя вводить знаки припенания и пробел в начале строки')
                    continue

                password = input('Введите пароль: ')
                if not self.is_suitable_string(password):
                    print('Нельзя вводить знаки припенания и пробел в начале строки')
                    continue

                el = self.return_el_with_login(all_data, login)

                if el is None:
                    print('Вы еще не зарегистрированны')
                    continue
                else:
                    if hashlib.sha256(password.encode()).hexdigest() == el.get('password', None):
                        new_password = self.random_password()
                        print('Поздравляю вы зашли!')
                        print(f'Ваш новый пароль: {new_password}')
                        self.return_el_with_login(all_data, login)['password'] = hashlib.sha256(
                            new_password.encode()).hexdigest()
                        self.load_to_file(main_file, all_data)
                    else:
                        print('Пароль не верный!')

            elif inputted == '2':

                try:
                    data = {
                        'login': self.is_suitable_raise(input('Введите логин: ')),
                        'password': hashlib.sha256(
                            self.is_suitable_raise(input('Введите пароль: ')).encode()).hexdigest(),
                        'FIO': self.is_suitable_raise(input('Введите ФИО: ')),
                        'main_word': self.is_suitable_raise(input('Введите ключевое слово: ')),
                    }
                except ValueError:
                    print('Нельзя вводить знаки припенания и пробел в начале строки')
                    continue
                # all_data = self.load_from_file(main_file)
                if self.return_el_with_login(all_data, data.get('login', None)) is None:
                    all_data.append(data)
                    self.load_to_file(main_file, all_data)
                    print('Регистрация завершена')
                else:
                    print('Человек с таким логином уже существует')
                    continue
            elif inputted == '3':
                login = input('Введите логин: ')
                if not self.is_suitable_string(login):
                    print('Нельзя вводить знаки припенания и пробел в начале строки')
                    continue
                main_word = input('Введите ключевое слово: ')
                if not self.is_suitable_string(main_word):
                    print('Нельзя вводить знаки припенания и пробел в начале строки')
                    continue
                self_el = self.return_el_with_login(all_data, login)
                if self_el is not None:
                    if self_el.get('main_word', None) == main_word:
                        new_password = self.random_password()
                        print('Поздравляю вы зашли!')

                        print(f'Ваш новый пароль: {new_password}')
                        self.return_el_with_login(all_data, login)['password'] = hashlib.sha256(
                            new_password.encode()).hexdigest()
                        self.load_to_file(main_file, all_data)
                    else:
                        print('Ключевое слово не верное')
                else:
                    print('Вы еще не зарегистрированны')


Main()
