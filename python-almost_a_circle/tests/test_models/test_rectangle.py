#!/usr/bin/python3
"""Test for rectangle model"""
import unittest
from io import StringIO
from unittest.mock import patch
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    def test_rectangle(self):
        r0 = Rectangle(1, 2)
        self.assertEqual(r0.width, 1)
        self.assertEqual(r0.height, 2)
        r1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)
        self.assertEqual(r1.id, 5)

    def test_type_errors(self):
        with self.assertRaises(TypeError):
            Rectangle()
        with self.assertRaises(TypeError):
            Rectangle(1)
        with self.assertRaises(TypeError):
            Rectangle("1", 2)
        with self.assertRaises(TypeError):
            Rectangle(1, "2")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")

    def test_value_errors(self):
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, -2)
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, 0)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_area(self):
        r0 = Rectangle(1, 2)
        self.assertEqual(r0.area(), 2)

    def test_str(self):
        r0 = Rectangle(1, 2, id=66)
        self.assertEqual(str(r0), "[Rectangle] (66) 0/0 - 1/2")

    def test_display1(self):
        r0 = Rectangle(2, 5)
        expected_output = "##\n##\n##\n##\n##\n"
        with patch("sys.stdout", new=StringIO()) as fake_out:
            r0.display()
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_display_2(self):
        r1 = Rectangle(2, 2)
        res = "##\n##\n"
        with patch("sys.stdout", new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

        r1.width = 5
        res = "#####\n#####\n"
        with patch("sys.stdout", new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_display_3(self):
        r1 = Rectangle(5, 4, 1, 1)
        res = "\n #####\n #####\n #####\n #####\n"
        with patch("sys.stdout", new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_display_4(self):
        r1 = Rectangle(3, 2)
        res = "###\n###\n"
        with patch("sys.stdout", new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

        r1.x = 4
        res = "    ###\n    ###\n"
        with patch("sys.stdout", new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

        r1.y = 2
        res = "\n\n    ###\n    ###\n"
        with patch("sys.stdout", new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_to_dictionary(self):
        r1 = Rectangle(3, 2)
        self.assertEqual(
            r1.to_dictionary(), {"id": 9, "width": 3, "height": 2, "x": 0, "y": 0}
        )

    def test_update(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")


if __name__ == "__main__":
    unittest.main()
