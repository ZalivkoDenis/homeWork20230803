# ШАГ. Д/з по сроку 03/08/2023 © Денис Заливко
"""
Создать класс User, у которого будут:
Имя
Фамилия
Логин (не менее 5 символов)
Пароль (не меньше 8 символов и должен содержать минимум 3 буквы).

Все поля должны быть скрытыми.
К каждому атрибуту написать по два метода.

Для вывода пользователя метод str не использовать.
"""


class User:

    def __init__(self, first_name: str, last_name: str, login: str, password: str = ""):
        self.first_name = first_name
        self.last_name = last_name
        self.login = login
        try:
            self.password = password
        except ValueError:
            print(f'{"-" * 40}\nОшибка!!!\nПользователь "{self.first_name} {self.last_name}" '
                  f'c логином "{self.login}" не создан.')
            raise

    @property
    def first_name(self) -> str:
        return self._first_name

    @first_name.setter
    def first_name(self, first_name: str):
        self._first_name = first_name

    @property
    def last_name(self) -> str:
        return self._last_name

    @last_name.setter
    def last_name(self, last_name: str):
        self._last_name = last_name

    @property
    def login(self) -> str:
        return self._login

    @login.setter
    def login(self, login: str):
        self._login = login

    @property
    def password(self) -> str:
        return self._password

    @password.setter
    def password(self, password: str):
        if password != '':  # Допускается пустой пароль (без пароля)
            if len(password) < 8:
                raise ValueError(f'({password}!!!) Пароль должен содержать не менее 8 символов')
            if len([c for c in password if c.isalpha()]) < 3:
                raise ValueError(f'({password}!!!) Пароль должен содержать не менее 3 букв')
        self._password = password

    def get_user_info(self, n: int = None) -> str:
        res = ('' if n is None else f'----- user-{str(n).zfill(3)} ').ljust(40, '-')
        res += f'\nИмя:\t\t{self.first_name}\nФамилия:\t{self.last_name}'
        res += f'\nЛогин:\t\t{self.login}\nПароль:\t\t'
        if self.password == '':
            res += '!!! Пароль пользователя отсутствует'
        else:
            res += f'{self.password}'
        return res + '\n'


if __name__ == '__main__':
    users: list[User] = []
    try:  # Пароль передаётся в __init__
        users.append(User('Denis', 'Zalivko', 'DenisZalivko', '123456qw'))
    except ValueError as ve:
        print(ve)

    user = User('Denis', 'Zalivko', 'DenisZalivko')  # user-001
    users.append(user)
    try:  # Пароль изменяется для существующего пользователя
        user.password = 'qwe345'
    except ValueError as ve:
        print(
            f'{"-" * 40}\nОшибка!!!\n'
            f'Пароль для пользователя "{user.first_name} {user.last_name}" c логином "{user.login}" '
            f'не изменён.')
        print(ve)

    try:
        users.append(User('Denis', 'Zalivko', 'DenisZalivko', 'qwerty12345'))  # user-002
    except ValueError as ve:
        print(ve)

    try:
        users.append(User('Aleksandr', 'Situn', 'AleksandrSitun'))  # user-003
    except ValueError as ve:
        print(ve)

    print(f'\n{"-" * 40}\n{"Пользователи:".center(40)}\n{"-" * 40}\n')
    for index in range(len(users)):
        print(users[index].get_user_info(index + 1))
