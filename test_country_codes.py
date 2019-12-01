import unittest
from country_codes import get_country_code
from pygal.maps.world import COUNTRIES


class CountryCodesTest(unittest.TestCase):
    def test_get_city_country(self):
        for i in COUNTRIES.items():
            country_code = get_country_code(i[1])
            self.assertEqual(country_code, i[0])


unittest.main()
