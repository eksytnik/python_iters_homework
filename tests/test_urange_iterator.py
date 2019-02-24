import unittest
from tests_homework.range_iterator import UrangeIter


class UserRangeTest(unittest.TestCase):
    def test_range_values(self):
        self.assertEqual(list(UrangeIter(4)), [0, 1, 2, 3])
        self.assertEqual(list(UrangeIter(40, 43)), [40, 41, 42])
        self.assertEqual(list(UrangeIter(1, 6, 2)), [1, 3, 5])
        self.assertEqual(list(UrangeIter(0, -30, -9)), [0, -9, -18, -27])

        self.assertEqual(list(UrangeIter(0)), [])
        self.assertEqual(list(UrangeIter(-10)), [])
        self.assertEqual(list(UrangeIter(10, 0)), [])
        self.assertEqual(list(UrangeIter(5, 1)), [])

    def test_iterator_exhausted(self):
        a = UrangeIter(2)
        self.assertEqual(next(a), 0)
        self.assertEqual(next(a), 1)
        self.assertRaises(StopIteration, next, a)
        self.assertRaises(StopIteration, next, a)
        b = UrangeIter(0)
        self.assertRaises(StopIteration, next, b)

    def test_range_errors(self):
        self.assertRaises(ValueError, UrangeIter, 1, 2, 0)  # 3rd argument can't be zero

        self.assertRaises(TypeError, UrangeIter, ())
        self.assertRaises(TypeError, UrangeIter, 1, 2, 3, 4)  # too many arguments

        self.assertRaises(TypeError, UrangeIter, 0.0, 1, 1)
        self.assertRaises(TypeError, UrangeIter, 0, 1.0, 1)
        self.assertRaises(TypeError, UrangeIter, 0, 1, 1.0)

        self.assertRaises(TypeError, UrangeIter, 'start', 2)
        self.assertRaises(TypeError, UrangeIter, 1, 'end')
        self.assertRaises(TypeError, UrangeIter, 1, 2, 'step')


if __name__ == '__main__':
    unittest.main()
