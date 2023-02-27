#!/usr/bin/python3

"""Test Module for the Rectangle class"""


import unittest
from models import rectangle
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    """Test cases for the Rectangle class"""

    def test_rectangle_instance_id(self):
        """Test Rectangle instance ID"""

        rect = Rectangle(10, 20)
        rect2 = Rectangle(15, 40, id=25)
        rect3 = Rectangle(20, 23, 5, 6)

        self.assertEqual(rect.id, 1)
        self.assertEqual(rect2.id, 25)
        self.assertEqual(rect3.id, 2)

    def test_rectangle_attributes_setters(self):
        """Setting Intance Attributes"""

        rect = Rectangle(34, 50, 10, 20, 23)

        self.assertEqual(rect.width, 34)
        self.assertEqual(rect.height, 50)
        self.assertEqual(rect.x, 10)
        self.assertEqual(rect.y, 20)
        self.assertEqual(rect.id, 23)

        rect.width = 4
        rect.height = 100
        rect.x = 2
        rect.y = 3

        self.assertEqual(rect.width, 4)
        self.assertEqual(rect.height, 100)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 3)

    def test_valid_integer_value_input(self):
        """Test Valid Integer Inputs"""

        rect = Rectangle(10, 15, 20, 30, 55)

        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 15)
        self.assertEqual(rect.x, 20)
        self.assertEqual(rect.y, 30)
        self.assertEqual(rect.id, 55)

    def test_invalid_integer_value_input(self):
        """Test Invalid Integer Inputs"""

        with self.assertRaises(ValueError, msg="width must be > 0", ):
            Rectangle(0, 15, 20, 30, 55)

        with self.assertRaises(ValueError, msg="width must be > 0", ):
            Rectangle(-50, 15, 20, 30, 55)

        with self.assertRaises(ValueError, msg="height must be > 0", ):
            Rectangle(10, 0, 20, 30, 55)

        with self.assertRaises(ValueError, msg="x must be >= 0", ):
            Rectangle(1, 15, -1, 30, 55)

        with self.assertRaises(ValueError, msg="y must be >= 0", ):
            Rectangle(1, 15, 14, -40, 55)

        self.assertEqual(Rectangle(1, 15, 14, 40, -55).id, -55)

    def test_invalid_type_input(self):
        """Test Invalid Type Inputs"""

        with self.assertRaises(TypeError, msg="width must be an integer", ):
            Rectangle("0", 15, 20, 30, 55)

        with self.assertRaises(TypeError, msg="width must be an integer", ):
            Rectangle([-50], 15, 20, 30, 55)

        with self.assertRaises(TypeError, msg="height must be an integer", ):
            Rectangle(10, {0: "height"}, 20, 30, 55)

        with self.assertRaises(TypeError, msg="x must be an integer", ):
            Rectangle(1, 15, ("Pos_x", 5), 30, 55)

        with self.assertRaises(TypeError, msg="y must be an integer", ):
            Rectangle(1, 15, 14, "Pos_y: 10", 55)

        self.assertEqual(Rectangle(1, 15, 14, 40, "Some_id").id, "Some_id")

    def test_area_calculation(self):
        """Tests for area of rectangle"""

        rect = Rectangle(3, 5, 5, 6, 7)
        rect2 = Rectangle(40, 3, 15, 20, 36)
        rect3 = Rectangle(12, 2, 40, 50, 19)

        self.assertEqual(rect.area(), 15)
        self.assertEqual(rect2.area(), 120)
        self.assertEqual(rect3.area(), 24)

    def test_string_repr_of_class(self):
        """Tests str representation of class"""

        rect = Rectangle(3, 5, 5, 6, 7)
        rect2 = Rectangle(40, 3, 15, 20, 36)
        rect3 = Rectangle(12, 2, 40, 5, 19)

        rect.display()
        rect2.display()
        rect3.display()

        self.assertEqual(str(rect), "[Rectangle] (7) 5/6 - 3/5")
        self.assertEqual(str(rect2), "[Rectangle] (36) 15/20 - 40/3")
        self.assertEqual(str(rect3), "[Rectangle] (19) 40/5 - 12/2")

    def test_attr_update(self, *args):
        """Test attribute updates"""

        rect = Rectangle(34, 50, 10, 20, 23)

        self.assertEqual(rect.width, 34)
        self.assertEqual(rect.height, 50)
        self.assertEqual(rect.x, 10)
        self.assertEqual(rect.y, 20)
        self.assertEqual(rect.id, 23)

        rect.update(49, 4, 100, 2, 3)

        self.assertEqual(rect.width, 4)
        self.assertEqual(rect.height, 100)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 3)
        self.assertEqual(rect.id, 49)

    def test_attr_update_with_invalid_type(self, *args):
        """Test attribute updates"""

        with self.assertRaises(TypeError, msg="width must be an integer", ):
            Rectangle(10, 15, 20, 30, 55).update(34, "34")

        with self.assertRaises(TypeError, msg="x must be an integer", ):
            Rectangle(50, 15, 20, 30, 55).update(34, 40, 40, "")

        with self.assertRaises(TypeError, msg="height must be an integer", ):
            Rectangle(10, 15, 20, 30, 55).update(34, 40, {"height": 10})

    def test_attr_update_with_kwargs(self, *args):
        """Test attribute updates using keyword args"""

        rect = Rectangle(34, 50, 10, 20, 23)

        self.assertEqual(rect.width, 34)
        self.assertEqual(rect.height, 50)
        self.assertEqual(rect.x, 10)
        self.assertEqual(rect.y, 20)
        self.assertEqual(rect.id, 23)

        rect.update(id=49, x=4, y=100, height=2, width=3)

        self.assertEqual(rect.width, 3)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 4)
        self.assertEqual(rect.y, 100)
        self.assertEqual(rect.id, 49)

    def test_serializers(self):
        """Test csv serializer"""

        rect = Rectangle(100, 45, 5, 6, 7)
        rect2 = Rectangle(40, 150, 15, 20, 36)
        rect3 = Rectangle(75, 200, 40, 5, 19)
        rect4 = Rectangle(75, 200, 40, 5, 19)

        objs = [rect, rect2, rect3]

        Rectangle.save_to_file_csv(objs)
        print(Rectangle.load_from_file_csv())


if __name__ == "__main__":
    unittest.main()
