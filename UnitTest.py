Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import unittest
... class TestAddNumbers(unittest,TestCase):
...     def test_addition(self):
...         self.assertEqual(add_numbers(1,2),3)
...         self.assertEqual(add_numbers(-1,1),0)
...         self.assertEqual(add_numbers(0,0),0)
...     if _name_=='_main_':
