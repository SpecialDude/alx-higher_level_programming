#!/usr/bin/python3

"""
Test for the Square class
"""


import unittest
from models.square import Square


class TestSquareClass(unittest.TestCase):
    """Tests for square class"""

    def test_square_instantiation(self):
        """Test instantiation of square"""

        sqr = Square(50, 10, 10, 7)

        self.assertEqual(sqr.width, sqr.height)
        self.assertEqual(sqr.id, 7)
        self.assertEqual(sqr.x, 10)
        self.assertEqual(sqr.y, 10)

        sqr.display()

    def test_string_repr_of_class(self):
        """Tests str representation of class"""

        sqr = Square(3, 5, 6, 7)
        sqr2 = Square(40, 15, 20, 36)
        sqr3 = Square(12, 40, 5, 19)

        sqr.display()
        sqr2.display()
        sqr3.display()

        self.assertEqual(str(sqr), "[Square] (7) 5/6 - 3")
        self.assertEqual(str(sqr2), "[Square] (36) 15/20 - 40")
        self.assertEqual(str(sqr3), "[Square] (19) 40/5 - 12")

    def test_size_instance_attribute(self):
        """Test for the size attribute of instances"""

        sqr = Square(3, 5, 6, 7)
        self.assertEqual(sqr.size, 3)

        sqr.size = 40
        self.assertEqual(sqr.size, 40)

        with self.assertRaises(TypeError, msg="width must be an integer"):
            sqr.size = "50"

        with self.assertRaises(ValueError, msg="width must be > 0"):
            sqr.size = -5

    def test_attr_update(self, *args):
        """Test attribute updates"""

        sqr = Square(34, 10, 20, 23)

        self.assertEqual(sqr.width, 34)
        self.assertEqual(sqr.height, 34)
        self.assertEqual(sqr.size, 34)
        self.assertEqual(sqr.x, 10)
        self.assertEqual(sqr.y, 20)
        self.assertEqual(sqr.id, 23)

        sqr.update(49, 100, 2, 3)

        self.assertEqual(sqr.width, 100)
        self.assertEqual(sqr.height, 100)
        self.assertEqual(sqr.size, 100)
        self.assertEqual(sqr.x, 2)
        self.assertEqual(sqr.y, 3)
        self.assertEqual(sqr.id, 49)

    def test_attr_update_with_invalid_type(self, *args):
        """Test attribute updates"""

        with self.assertRaises(TypeError, msg="width must be an integer", ):
            Square(10, 20, 30, 55).update(34, "34")

        with self.assertRaises(TypeError, msg="x must be an integer", ):
            Square(50, 20, 30, 55).update(34, 40, "")

    def test_attr_update_with_kwargs(self, *args):
        """Test attribute updates using keyword args"""

        sqr = Square(34, 10, 20, 23)

        self.assertEqual(sqr.width, 34)
        self.assertEqual(sqr.height, 34)
        self.assertEqual(sqr.x, 10)
        self.assertEqual(sqr.y, 20)
        self.assertEqual(sqr.id, 23)

        sqr.update(id=49, x=4, y=100, size=2)

        self.assertEqual(sqr.width, 2)
        self.assertEqual(sqr.height, 2)
        self.assertEqual(sqr.x, 4)
        self.assertEqual(sqr.y, 100)
        self.assertEqual(sqr.id, 49)

    def test_serializers(self):
        """Test csv serializer"""

        sqr = Square(3, 5, 6, 7)
        sqr2 = Square(40, 15, 20, 36)
        sqr3 = Square(12, 40, 5, 19)

        objs = [sqr, sqr2, sqr3]

        Square.save_to_file_csv(objs)
        print(Square.load_from_file_csv())


if __name__ == "__main__":
    unittest.main()
