import unittest
from factorial import factorial


class TestFactorial(unittest.TestCase):

    def test_fact(self):
        res = factorial(5)
        self.assertEqual(res, 120)


if __name__ == '__main__':
    unittest.main()
