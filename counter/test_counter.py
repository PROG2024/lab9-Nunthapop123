"""Write a unit test to verify that Counter is a singleton.

   Also verify that all instances share the same count
   and that the count is not reset to 0 when you invoke 
   count = Counter() 
   after the first time.

   You can use pytest or unittest.
"""

import unittest
from counter import Counter


class TestCounter(unittest.TestCase):

    def test_is_it_singleton(self):
        """ all instances should be the same """
        self.counter = Counter()
        self.counter2 = Counter()
        self.assertTrue(self.counter, self.counter2)

    def test_references_share_the_same_count(self):
        """all instance should share the same count"""
        self.counter = Counter()
        self.assertEqual(self.counter.count, 0)
        self.counter.increment()
        self.assertEqual(self.counter.count, 1)
        self.counter2 = Counter()
        self.assertEqual(self.counter2.count, 1)
        self.assertEqual(self.counter.count, self.counter2.count)
