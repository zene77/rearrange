#!/usr/bin/env python3
import unittest
from rearrange import rearrange_name

class TestRearrange(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(rearrange_name("Lovelace, Ada"), "Ada Lovelace")

if __name__ == '__main__':
    unittest.main()
