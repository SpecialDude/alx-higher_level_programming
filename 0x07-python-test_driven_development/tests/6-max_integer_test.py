import unittest

class MaxIntegerTests(unittest.TestCase):

    def setUp(self):
        self.max_integer = __import__("6-max_integer").max_integer

    def test_empty_list(self):
        result = self.max_integer()
        self.assertIsNone(result)

        result = self.max_integer([])

        self.assertIsNone(result)

    def test_list_of_same_values(self):
        result = self.max_integer([3, 3, 3, 3])
        self.assertEqual(result, 3)

if __name__ == "__main__":
    unittest.main