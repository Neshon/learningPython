import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    """Тесты для класса Employee"""
    def setUp(self):
        """Создание экземпляра класса, сумму увеличение зарплаты и
        ожидаемое значение зарплаты"""
        self.andi = Employee('Bob', 'Regan', 13520)
        self.salary_increase = 10000
        self.salary = [18520, 23520]

    def test_give_default_raise(self):
        """Увеличение зарплаты по умолчанию"""
        self.assertEqual(self.salary[0], self.andi.give_raise())

    def test_give_custom_raise(self):
        """Увеличение зарплаты на заданное значение salary_increase"""
        self.assertEqual(self.salary[1],
                         self.andi.give_raise(self.salary_increase))


unittest.main()
