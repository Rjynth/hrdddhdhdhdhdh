import unittest
# задание https://netology.ru/profile/program/py-92/lessons/300096/lesson_items/1622441

def check_age(age: int) -> str:
    if age >= 18:
        result = 'Доступ разрешён'
    else:
        result = 'Доступ запрещён'
    return result

class TestCheckAge(unittest.TestCase):
    def test_age_10(self):
        self.assertEqual(check_age(10), 'Доступ запрещён')

    def test_age_20(self):
        self.assertEqual(check_age(20), 'Доступ разрешён')

    def test_age_negative(self):
        self.assertEqual(check_age(-5), 'Доступ запрещён')

    def test_age_18(self):
        self.assertEqual(check_age(18), 'Доступ разрешён')

if __name__ == '__main__':
    unittest.main()
