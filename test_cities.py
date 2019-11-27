import unittest
from city_functions import get_city_country


class CityFuncTest(unittest.TestCase):
    def test_get_city_country(self):
        city_country = get_city_country('santiago', 'chile')
        self.assertEqual(city_country, 'Santiago, Chile')

    def test_get_city_country_population(self):
        city_country = get_city_country('santiago', 'chile', '50000')
        self.assertEqual(city_country, 'Santiago, Chile - population 50000')


unittest.main()
