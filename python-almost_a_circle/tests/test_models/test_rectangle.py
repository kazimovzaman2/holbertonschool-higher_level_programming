#!/usr/bin/python3
"""Test for rectangle model"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    def test_rectangle(self):
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 1)
        self.assertEqual(str(r1), "[Rectangle] (1) 0/0 - 1/2")


if __name__ == "__main__":
    unittest.main()
