#!/usr/bin/python3
"""Test for rectangle model"""
import unittest
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    def test_rectangle(self):
        r0 = Rectangle(1, 2)
        self.assertEqual(r0.width, 1)
        self.assertEqual(r0.height, 2)
        with self.assertRaises(TypeError):
            r1 = Rectangle("1", 2)
            r2 = Rectangle(1, "2")
            r3 = Rectangle(1, 2, "3")
            r4 = Rectangle(1, 2, 3, "4")


if __name__ == "__main__":
    unittest.main()
