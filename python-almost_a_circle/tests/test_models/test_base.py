#!/usr/bin/python3
"""Test for base model"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_init(self):
        base = Base()
        self.assertIsInstance(base, Base)
        self.assertEqual(base.id, 1)

    def test_id_exists(self):
        base = Base()
        self.assertTrue(hasattr(base, "id"))


if __name__ == "__main__":
    unittest.main()
