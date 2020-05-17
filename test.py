import unittest
from hello import *

class MyTests(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello("andrei"), "approved by: andrei")
    def test_hello_roxana(self):
        self.assertEqual(hello("roxana"), "approved by: roxana")
    def test_hello_empty(self):
        self.assertEqual(hello(), "approved by: mata")

if __name__=="__main__":
    unittest.main()
