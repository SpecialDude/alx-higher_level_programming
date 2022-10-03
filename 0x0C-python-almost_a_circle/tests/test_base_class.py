#!/usr/bin/python3

"""Tests for the Base Class"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseClass(unittest.TestCase):
    """Test class for Base"""

    def test_new_intsance_without_id(self):
        """Test New instance creation without id"""

        base = Base()
        base2 = Base()
        base3 = Base()

        self.assertEqual(base.id, 4)
        self.assertEqual(base2.id, 5)
        self.assertEqual(base3.id, 6)

    def test_new_intsance_with_id(self):
        """Test New instance creation with id"""
        base = Base(id=5)
        base2 = Base(10)
        base3 = Base(25)


        self.assertEqual(base.id, 5)
        self.assertEqual(base2.id, 10)
        self.assertEqual(base3.id, 25)

    def test_new_intsance(self):
        """Test New instance creation"""

        base = Base(id=98)
        base2 = Base()
        base3 = Base()
        base4 = Base(33)
        base5 = Base()
        base6 = Base(56)


        self.assertEqual(base.id, 98)
        self.assertEqual(base2.id, 1)
        self.assertEqual(base3.id, 2)
        self.assertEqual(base4.id, 33)
        self.assertEqual(base5.id, 3)
        self.assertEqual(base6.id, 56)

    def test_shape_draw(self):
        rect = Rectangle(100, 33, 0, 0, 10)
        sqr = Square(55, 4, 80, 89)

        Base.draw([rect], [sqr])

if __name__ == "__main__":
    unittest.main()