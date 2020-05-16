import unittest
from hello import *

class MyTests(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello(), "approved by: andrei")
