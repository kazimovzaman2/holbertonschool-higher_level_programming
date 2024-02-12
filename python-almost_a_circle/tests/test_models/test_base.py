#!/usr/bin/python3
"""Test for base model"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_id_as_positive(self):
        base_instance = Base(115)
        self.assertEqual(base_instance.id, 115)
        base_instance = Base(67)
        self.assertEqual(base_instance.id, 67)

    def test_id_as_negative(self):
        base_instance = Base(-91)
        self.assertEqual(base_instance.id, -91)
        base_instance = Base(-4)
        self.assertEqual(base_instance.id, -4)

    def test_id_as_none(self):
        base_instance = Base()
        self.assertEqual(base_instance.id, 1)
        base_instance = Base(None)
        self.assertEqual(base_instance.id, 2)

    def test_string_id(self):
        base_instance = Base("Monty Python")
        self.assertEqual(base_instance.id, "Monty Python")
        base_instance = Base("Python is cool")
        self.assertEqual(base_instance.id, "Python is cool")


if __name__ == "__main__":
    unittest.main()
