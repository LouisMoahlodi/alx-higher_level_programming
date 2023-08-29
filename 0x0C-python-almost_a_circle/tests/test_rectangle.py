import unittest
import json
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def test_init_with_id(self):
        r1 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.id, 12)

    def test_init_without_id(self):
        r1 = Rectangle(10, 2, 0, 0)
        self.assertEqual(r1.id, 1)

    def test_width(self):
        r1 = Rectangle(10, 2, 0, 0)
        self.assertEqual(r1.width, 10)

    def test_height(self):
        r1 = Rectangle(10, 2, 0, 0)
        self.assertEqual(r1.height, 2)

    def test_x(self):
        r1 = Rectangle(10, 2, 0, 0)
        self.assertEqual(r1.x, 0)
    
    def test_y(self):
        r1 = Rectangle(10, 2, 0, 0)
        self.assertEqual(r1.y, 0)

    def test_width_typeerror(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle("10", 2, 0, 0)

    def test_height_typeerror(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, "2", 0, 0)

    def test_x_typeerror(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, 2, "0", 0)
    
    def test_y_typeerror(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, 2, 0, "0")

    def test_width_valueerror(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(-10, 2, 0, 0)

    def test_height_valueerror(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(10, -2, 0, 0)

    def test_x_valueerror(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(10, 2, -1, 0)
    
    def test_y_valueerror(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(10, 2, 0, -1)
    
    def test_area(self):
        r1 = Rectangle(10, 2, 0, 0)
        self.assertEqual(r1.area(), 20)