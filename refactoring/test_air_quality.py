"""Tests of air_quality function"""
import unittest
from solution.air_quality import air_quality

class AirQualityTest(unittest.TestCase):

    def test_clean_air(self):
        data = [5, 9.99, 0]
        self.assertEqual("very good", air_quality(data))

    def test_singleton(self):
        """only a single measurement should be ok"""
        data = [10.1]
        self.assertEqual("good", air_quality(data))

    def test_one_high_measurement(self):
        data = [0, 0, 5, 5, 99]
        self.assertEqual("good", air_quality(data))

    def test_one_dangerous_measurement(self):
        data = [0, 0, 5, 250, 4]
        self.assertEqual("dangerously unhealthy", air_quality(data))

    def test_poor_air(self):
        data = [0, 0, 125, 175, 150, 180]
        self.assertEqual("poor", air_quality(data))

    def test_bangkok_air(self):
        data = [0, 175, 180, 175, 180, 190, 180]
        self.assertEqual("unhealthy", air_quality(data))

if __name__ == '__main__':
    unittest.main(verbosity=2)
