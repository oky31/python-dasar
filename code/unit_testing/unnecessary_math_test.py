import unittest
from unnecessary_math import multiply

class TestUM(unittest.TestCase):

    def test_number_3_4(self):
        self.assertEqual(multiply(3,4), 12)