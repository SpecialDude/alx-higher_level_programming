#!/usr/bin/python3

"""
Tests for the module to find the max integer in a list
"""

import unittest


class MaxIntegerTests(unittest.TestCase):
    """Max Integer Tests"""

    def setUp(self):
        """Tests Setup"""

        self.max_integer = __import__("6-max_integer").max_integer

    def test_empty_list(self):
        """Test an Empty List"""

        result = self.max_integer()
        self.assertIsNone(result)

        result = self.max_integer([])

        self.assertIsNone(result)

    def test_list_of_same_values(self):
        """Test list with same Elements"""

        result = self.max_integer([3, 3, 3, 3])
        self.assertEqual(result, 3)

        result = self.max_integer([0])
        self.assertEqual(result, 0)

        result = self.max_integer([0, 0])
        self.assertEqual(result, 0)


    def test_list_of_distinct_values(self):
        """Test list with distint Elements"""

        li = [1, 2, 3, 4, 6]
        result = self.max_integer(li)
        self.assertEqual(result, max(li))

        li = [3, 8, 9, 0, 3, 9, 0, 16]
        result = self.max_integer(li)
        self.assertEqual(result, max(li))

        li = [0, -9, -7, -2]
        result = self.max_integer(li)
        self.assertEqual(result, max(li))

        li = [1.9, 2.8, -17.9, -2.2]
        result = self.max_integer(li)
        self.assertEqual(result, max(li))

    def test_with_list_of_str_types(self):
        """Test list with Non-integer (str) Elements"""

        li = ["Ade", "John", "Bull"]
        result = self.max_integer(li)
        self.assertEqual(result, max(li))

    def test_with_list_of_mixed_types(self):
        """Test list with mixed type Elements"""

        li = ["Ade", "John", "Bull", 35, 90]

        with self.assertRaises(TypeError):
            result = self.max_integer(li)

    def test_with_non_list_argument(self):
        """Test with non-list argument"""

        with self.assertRaises(TypeError):
            self.max_integer(5)

        with self.assertRaises(TypeError):
            self.max_integer(None)

if __name__ == "__main__":
    unittest.main()