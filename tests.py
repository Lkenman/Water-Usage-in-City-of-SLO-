import unittest
from class_city import City


class TestCityWaterUsage(unittest.TestCase):
    def setup(self):
        self.test_city_efficient = City("San Luis Obispo", "CA", 47000, 5640000)
        self.test_city_wasteful = City("Bakersfield", "CA", 162570, )


if __name__ == '__main__':
    unittest.main()
