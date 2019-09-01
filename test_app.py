import unittest

from app import dummy

class TestDummy(unittest.TestCase):

    def test_dummy(self):
        self.assertEqual(dummy(1), 1)
        self.assertEqual(dummy(2), 2)
        self.assertEqual(dummy(3), 3)
        self.assertEqual(dummy(3), 3)