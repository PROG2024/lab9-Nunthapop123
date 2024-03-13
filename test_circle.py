"""Unit tests of the Circle class using unittest or pytest (your choice).

Write unit tests as described in README.md.

1. Unit test for add_area using typical values.
2. Unit test for add_area for an "edge case" where one circle has radius 0.
3. Unit test that circle constructor raises exception of radius is negative.

"""
from circle import Circle
import unittest
import math


class TestCircle(unittest.TestCase):

    def test_add_typical_value(self):
        """try add an area by typical value"""
        circle1 = Circle(3)
        circle2 = Circle(4)
        new_circle = circle1.add_area(circle2)
        self.assertEqual(5, new_circle.get_radius())
        self.assertEqual(math.pi * 5 * 5, new_circle.get_area())

    def test_add_only_one_value(self):
        """try add an area by a circle with zero radius"""
        circle1 = Circle(3)
        circle2 = Circle(0)
        new_circle = circle1.add_area(circle2)
        self.assertEqual(3, new_circle.get_radius())
        self.assertEqual(math.pi * 3 * 3, new_circle.get_area())

    def test_circle_have_negative_radius(self):
        """circle cannot have negative radius"""
        with self.assertRaises(Exception):
            Circle(-1)

if __name__ == '__main__':
    unittest.main()
