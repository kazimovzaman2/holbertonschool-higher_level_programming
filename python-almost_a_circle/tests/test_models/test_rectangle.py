#!/usr/bin/python3
"""Test for rectangle model"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    def test_rectangle(self):
        r1 = Rectangle(1, 2, id=3)
        self.assertIsNotNone(r1)


if __name__ == "__main__":
    unittest.main()
