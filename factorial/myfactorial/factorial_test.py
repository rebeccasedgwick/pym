import unittest
from factorial import factorial, div


class TestFactorial(unittest.TestCase):

    def test_fact(self):
        res = factorial(5)
        self.assertEqual(res, 120)

    def test_error(self):
        """
        Test if exception raised due to runtime error: division by 0
        """
        self.assertRaises(ZeroDivisionError, div, 0)


if __name__ == '__main__':
    unittest.main()
