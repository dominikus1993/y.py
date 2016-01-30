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

    def test_map(self):
        test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        test_mapper = lambda x: x + 1

        test_result = y.map(test_list, test_mapper)
        self.assertListEqual(test_result, [2, 3, 4, 5, 6, 7, 8, 9, 10, 11])

    def test_reduce(self):
        test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        test_reductor = lambda acc, x: acc + x

        test_result = y.reduce(test_list, test_reductor, 0)
        self.assertEqual(test_result, 55)

    def test_first(self):
        test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        test_predicate = lambda x: x % 2 == 0
        test_result = y.first(test_list, test_predicate)
        self.assertEqual(test_result, 2)

        # invalid predicate
        test_predicate2 = lambda x: x == 12
        self.assertRaises(Exception, lambda: y.first(test_list, test_predicate2))
