import unittest, sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from urange_generator import urange


class UserRangeTest(unittest.TestCase):
    def test_range_values(self):
        self.assertEqual(list(urange(4)), [0, 1, 2, 3])
        self.assertEqual(list(urange(40, 43)), [40, 41, 42])
        self.assertEqual(list(urange(1, 6, 2)), [1, 3, 5])
        self.assertEqual(list(urange(0, -30, -9)), [0, -9, -18, -27])

        self.assertEqual(list(urange(0)), [])
        self.assertEqual(list(urange(-10)), [])
        self.assertEqual(list(urange(10, 0)), [])
        self.assertEqual(list(urange(5, 1)), [])


    def test_range_errors(self):
        with self.assertRaises(ValueError):
            list(urange(1, 2, 0))  # 3rd argument can't be zero

        with self.assertRaises(TypeError):
            list(urange())
        with self.assertRaises(TypeError):
            list(urange(1, 2, 3, 4))  # too many arguments

        with self.assertRaises(TypeError):
            list(urange(0.0, 1, 1))
        with self.assertRaises(TypeError):
            list(urange(0, 1.0, 1))
        with self.assertRaises(TypeError):
            list(urange(0, 1, 1.0))

        with self.assertRaises(TypeError):
            list(urange('start', 2))
        with self.assertRaises(TypeError):
            list(urange(1, 'end'))
        with self.assertRaises(TypeError):
            list(urange(1, 2, 'step'))


if __name__ == '__main__':
    unittest.main()
