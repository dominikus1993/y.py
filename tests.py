from unittest import TestCase
import y


class Tests(TestCase):
    def test_range(self):
        start = 1
        end = 10
        test_result = y.range(start, end)
        self.assertEqual(len(test_result), 10)
        self.assertEqual(test_result[-1], 10)
        self.assertEqual(test_result[0], 1)
