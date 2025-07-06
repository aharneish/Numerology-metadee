import unittest
from numerology import get_life_path, get_destiny, get_soul_urge, get_numerology_profile

class TestNumerology(unittest.TestCase):
    """
    Unit tests for numerology calculations and input validation.
    Each test prints the actual output for easier debugging.
    """
    def test_valid_life_path(self):
        # Test correct calculation of life path number for valid dates
        result1 = get_life_path('2001-12-25')
        result2 = get_life_path('1999-11-22')
        print(f"get_life_path('2001-12-25') = {result1}")
        print(f"get_life_path('1999-11-22') = {result2}")
        self.assertEqual(result1, 4)
        self.assertEqual(result2, 7)

    def test_invalid_date_format(self):
        # Test that invalid date formats and impossible dates raise ValueError
        with self.assertRaises(ValueError):
            get_life_path('01-12-25')
        with self.assertRaises(ValueError):
            get_life_path('2001/12/25')
        with self.assertRaises(ValueError):
            get_life_path('2001-13-01')  # Invalid month
        with self.assertRaises(ValueError):
            get_life_path('2025-02-30')  # Invalid day
        with self.assertRaises(ValueError):
            get_life_path("366666-333333-111")

    def test_destiny_and_soul_urge(self):
        # Test correct calculation of destiny and soul urge numbers
        destiny = get_destiny('Aharneish')
        soul_urge = get_soul_urge('Abburu')
        print(f"get_destiny('Aharneish') = {destiny}")
        print(f"get_soul_urge('Abburu') = {soul_urge}")
        self.assertEqual(destiny, 7)
        self.assertEqual(soul_urge, 7)

    def test_numerology_profile_valid(self):
        # Test numerology profile output for valid input
        profile = get_numerology_profile('Aharneish', '2001-12-25')
        print(f"get_numerology_profile('Aharneish', '2001-12-25') = {profile}")
        self.assertEqual(profile['life_path'], 4)
        self.assertEqual(profile['destiny'], 7)
        self.assertEqual(profile['soul_urge'], 7)
        self.assertFalse(profile['is_master'])

    def test_numerology_profile_invalid_date(self):
        # Test that invalid date in numerology profile raises ValueError
        with self.assertRaises(ValueError):
            get_numerology_profile('Aharneish', '2025-02-30')

if __name__ == '__main__':
    unittest.main()
