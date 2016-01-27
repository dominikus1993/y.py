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

    def test_filter(self):
        test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        test_predicate = lambda x: x % 2 == 0
        test_result = y.filter(test_list, test_predicate)
        self.assertListEqual(test_result, [2, 4, 6, 8, 10])

    def test_each(self):
        test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        def test_callback(x):
            y = x + 1
            self.assertEqual(x + 1, y)
            return x

        test_result = y.each(test_list, test_callback)
