import unittest
from main import add, subtract, multiply

class TestMainFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(-5, 3), -2)
    
    def test_subtract(self):
        self.assertEqual(subtract(10, 4), 6)
        self.assertEqual(subtract(10, -4), 14)
    
    def test_multiply(self):
        self.assertEqual(multiply(2, 6), 12)
        self.assertEqual(multiply(5, 0), 0)

if __name__ == '__main__':
    unittest.main()