import unittest
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

        # invalid start and end
        bad_start = 10
        bad_end = 1
        self.assertRaises(Exception, lambda: y.range(bad_start, bad_end))

    def test_filter(self):
        test_list = [1, 2, 3, 4, 5, 6]
        test_predicate = lambda x: x % 2 == 0
        test_result = y.filter(test_list, test_predicate)
        self.assertListEqual(test_result, [2, 4, 6])

    def test_each(self):
        test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        def test_callback(x):
            y = x + 1
            self.assertEqual(x + 1, y)
            return x

        test_result = y.each(test_list, test_callback)

    def test_map(self):
        test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        test_mapper = lambda x: x + 1

        test_result = y.map(test_list, test_mapper)
        self.assertListEqual(test_result, [2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

    def test_reduce(self):
        test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        def test_reducer(acc, x):
            return acc + x

        test_result = y.reduce(test_list, test_reducer, 0)
        self.assertEqual(test_result, 55)

    def test_first(self):
        test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        def test_predicate(x):
            return x % 2 == 0

        test_result = y.first(test_list, test_predicate)
        self.assertEqual(test_result, 2)

        # invalid predicate
        def test_predicate2(x):
            return x == 12

        self.assertRaises(Exception, lambda: y.first(test_list, test_predicate2))

    def test_reject(self):
        test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        test_predicate = lambda x: x % 2 == 0
        test_result = y.reject(test_list, test_predicate)
        self.assertListEqual(test_result, [1, 3, 5, 7, 9])

    def test_every(self):
        test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        test_predicate = lambda x: x % 2 == 0 or x % 2 == 1
        test_result = y.every(test_list, test_predicate)
        self.assertTrue(test_result)

        # invalid predicate
        test_predicate = lambda x: x % 2 == 0
        test_result = y.every(test_list, test_predicate)
        self.assertFalse(test_result)

    def test_some(self):
        test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        test_predicate = lambda x: x == 1
        test_result = y.some(test_list, test_predicate)
        self.assertTrue(test_result)

        # invalid predicate
        test_predicate = lambda x: x == 222
        test_result = y.some(test_list, test_predicate)
        self.assertFalse(test_result)

    def test_contains(self):
        test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        test_result = y.contains(test_list, 1)
        self.assertTrue(test_result)

        # invalid predicate
        test_result = y.contains(test_list, 11111)
        self.assertFalse(test_result)

    def test_max(self):
        test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        test_iterate = lambda x: x
        test_result = y.max(test_list, test_iterate)
        self.assertEqual(test_result, 10)

    def test_min(self):
        test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        test_iterate = lambda x: x
        test_result = y.min(test_list, test_iterate)
        self.assertEqual(test_result, 1)

        test_list = [2, 3, 4, 5, 1, 6, 7, 8, 9, 10]
        test_iterate = lambda x: x
        test_result = y.min(test_list, test_iterate)
        self.assertEqual(test_result, 1)

    def test_size(self):
        test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        test_result = y.size(test_list)
        self.assertEqual(test_result, 10)

    def test_sample(self):
        test_list = [2, 3, 4, 5, 1, 6, 7, 8, 9, 10]
        test_result = y.sample(test_list, 3)
        self.assertEqual(len(test_result), 3)

    def test_partition(self):
        test_list = [2, 3, 4, 5, 1, 6, 7, 8, 9, 10]

        def test_predicate(num):
            return num % 2 == 0

        test_result = y.partition(test_list, test_predicate)
        self.assertListEqual(test_result[0], [2, 4, 6, 8, 10])
        self.assertListEqual(test_result[1], [3, 5, 1, 7, 9])

    def test_sort_by(self):
        test_list = [1, 6, 8, 7, 14, 45, 6]
        test_result = y.sort_by(test_list)
        self.assertListEqual(test_result, [1, 6, 6, 7, 8, 14, 45])

    def test_last(self):
        test_list = [5, 4, 3, 2, 1]
        test_result = y.last(test_list)
        self.assertEqual(test_result, 1)

        test_list = []
        test_result = y.last(test_list)
        self.assertListEqual(test_result, [])

    def test_without(self):
        test_list = [1, 2, 1, 0, 3, 1, 4]
        test_result = y.without(test_list, 0, 1)
        self.assertListEqual(test_result, [2, 3, 4])

    def test_rest(self):
        test_list = [5, 4, 3, 2, 1]
        test_result = y.rest(test_list)
        self.assertListEqual(test_result, [4, 3, 2, 1])

    def test_initial(self):
        test_list = [5, 4, 3, 2, 1]
        test_result = y.initial(test_list)
        self.assertListEqual(test_result, [5, 4, 3, 2])

        test_result = y.initial(test_list, 5555)
        self.assertListEqual(test_result, [])

    def test_exist(self):
        test_list = [5, 4, 3, 2, 1]
        test_result = y.exist(test_list, 1)
        self.assertTrue(test_result)

        test_result = y.exist(test_list, 1545454)
        self.assertFalse(test_result)

    def test_unique(self):
        test_list = [1, 2, 1, 4, 1, 3]
        test_result = y.unique(test_list)
        self.assertListEqual(test_result, [1, 2, 4, 3])


if __name__ == '__main__':
    unittest.main()
