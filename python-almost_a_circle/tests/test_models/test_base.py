#!/usr/bin/python3
"""Test for base model"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_init(self):
        base = Base()
        self.assertIsInstance(base, Base)
        self.assertEqual(base.id, 1)

        base2 = Base()
        self.assertIsInstance(base2, Base)
        self.assertEqual(base2.id, 2)

        base3 = Base(10)
        self.assertIsInstance(base3, Base)
        self.assertEqual(base3.id, 10)

    def test_auto_assign_id(self):
        base1 = Base()
        base2 = Base()
        base3 = Base()
        self.assertEqual(base1.id, 3)
        self.assertEqual(base2.id, 4)
        self.assertEqual(base3.id, 5)

    def test_id_exists(self):
        base = Base(100)
        self.assertEqual(base.id, 100)


if __name__ == "__main__":
    unittest.main()
