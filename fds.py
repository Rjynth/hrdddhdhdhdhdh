import unittest
# задание https://netology.ru/profile/program/py-92/lessons/300096/lesson_items/1622443
def get_cost(weight: int) -> str:
    if weight <= 10:
        result = "Стоимость доставки: 200 руб."
    else:
        result = "Стоимость доставки: 500 руб."
    return result

class TestGetCost(unittest.TestCase):
    def test_weight_9(self):
        self.assertIn('200', get_cost(9))

    def test_weight_12(self):
        self.assertIn('500', get_cost(12))

    def test_weight_negative(self):
        self.assertIn('500', get_cost(-5))

if __name__ == '__main__':
    unittest.main()
