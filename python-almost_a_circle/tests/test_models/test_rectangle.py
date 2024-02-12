#!/usr/bin/python3
"""Test for rectangle model"""
import unittest
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    def test_rectangle(self):
        r0 = Rectangle(1, 2)
        self.assertEqual(r0.width, 1)
        self.assertEqual(r0.height, 2)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_no_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_string_arg(self):
        with self.assertRaises(TypeError):
            Rectangle("1", 2)


if __name__ == "__main__":
    unittest.main()
