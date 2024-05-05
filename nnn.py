import unittest
# задание https://netology.ru/profile/program/py-92/lessons/300096/lesson_items/1622442
def check_auth(login: str, password: str) -> str:
    if login == "admin" and password == "password":
        result = "Добро пожаловать"
    else:
        result = "Доступ ограничен"
    return result

class TestCheckAuth(unittest.TestCase):
    def test_invalid_login(self):
        self.assertEqual(check_auth('user', 'password'), 'Доступ ограничен')

    def test_invalid_password(self):
        self.assertEqual(check_auth('admin', '123'), 'Доступ ограничен')

    def test_valid_credentials(self):
        self.assertEqual(check_auth('admin', 'password'), 'Добро пожаловать')

if __name__ == '__main__':
    unittest.main()
