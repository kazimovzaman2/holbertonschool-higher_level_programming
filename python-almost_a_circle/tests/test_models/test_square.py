#!/usr/bin/python3
"""Test for rectangle model"""
import unittest
from models.square import Square


class TestBase(unittest.TestCase):
    def test_square(self):
        s0 = Square(1, 2, 3, 4)
        self.assertEqual(s0.size, 1)
        self.assertEqual(s0.x, 2)
        self.assertEqual(s0.y, 3)
        self.assertEqual(s0.id, 4)

    def test_type_errors(self):
        with self.assertRaises(TypeError):
            Square()
        with self.assertRaises(TypeError):
            Square("1")
        with self.assertRaises(TypeError):
            Square(1, "2")
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_value_errors(self):
        with self.assertRaises(ValueError):
            Square(-1)
        with self.assertRaises(ValueError):
            Square(1, -2)
        with self.assertRaises(ValueError):
            Square(1, 2, -3)
        with self.assertRaises(ValueError):
            Square(0)

    def test_str(self):
        s0 = Square(1, id=66)
        self.assertEqual(str(s0), "[Square] (66) 0/0 - 1")

    def test_to_dictionary(self):
        s1 = Square(3, id=55)
        self.assertEqual(s1.to_dictionary(), {"id": 55, "size": 3, "x": 0, "y": 0})

    def test_update(self):
        s0 = Square(1, 2, 3, 4)
        s0.update(5, 6, 7, 8)
        self.assertEqual(s0.id, 5)
