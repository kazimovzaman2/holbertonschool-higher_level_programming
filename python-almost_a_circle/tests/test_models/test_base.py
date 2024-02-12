#!/usr/bin/python3
"""Test for base model"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_init(self):
        base = Base()
        self.assertIsInstance(base, Base)
        self.assertEqual(base.id, 1)


if __name__ == "__main__":
    unittest.main()
