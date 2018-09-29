import unittest
from unittest import TestCase
#Coverage Testing of Routing.py

class TestGetCheapestOperator(TestCase):
    def test_getCheapestOperator(self):
        from Routing import getCheapestOperator
        self.assertTrue(getCheapestoperator(44))

    def test_getCheapestOperator(self):
        from Routing import getCheapestOperator
        self.assertFalse(getCheapestoperator(2))

if __name__ == '__main__':
    unittest.main()
    