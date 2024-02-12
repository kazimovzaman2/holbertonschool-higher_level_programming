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

    def test_to_json_string(self):
        base = Base()
        json_string = base.to_json_string([])
        self.assertEqual(json_string, "[]")

    def test_from_json_string(self):
        json_string = "[]"
        list_dictionaries = Base.from_json_string(json_string)
        self.assertEqual(list_dictionaries, [])

    def test_create(self):
        dictionary = {"id": 1}
        base = Base.create(**dictionary)
        self.assertIsInstance(base, Base)
        self.assertEqual(base.id, 1)


if __name__ == "__main__":
    unittest.main()
