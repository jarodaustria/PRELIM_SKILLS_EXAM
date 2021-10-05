import unittest
from B_script import Temperature

class test_b(unittest.TestCase):
    def test_25(self):
        '''Answer should be 25'''
        self.assertTrue(25==Temperature(25).kelvin)
    def test_20(self):
        '''Answer should be 25'''
        self.assertTrue(20==Temperature(20).kelvin)
    def test_15(self):
        '''Answer should be 25'''
        self.assertTrue(15==Temperature(15).kelvin)
    def test_10(self):
        '''Answer should be 25'''
        self.assertTrue(10==Temperature(10).kelvin)

if __name__ == "__main__":
    unittest.main(argv=[''],  verbosity=2)