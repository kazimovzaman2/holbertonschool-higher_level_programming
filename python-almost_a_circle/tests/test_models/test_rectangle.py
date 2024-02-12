#!/usr/bin/python3
"""Test for rectangle model"""
import unittest
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    def test_rectangle(self):
        r0 = Rectangle(1, 2, id=1)
        self.assertEqual(r0.id, 1)
        r1 = Rectangle(2, 3, id=12)
        self.assertEqual(r1.id, 12)


if __name__ == "__main__":
    unittest.main()
