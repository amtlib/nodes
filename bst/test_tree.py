import unittest
from tree.tree import Tree


class TestTreeMethods(unittest.TestCase):

    def setUp(self):
        self.tree = Tree()
        # Values from the task
        self.tree.add_value(5)
        self.tree.add_value(3)
        self.tree.add_value(2)
        self.tree.add_value(5)
        self.tree.add_value(7)
        self.tree.add_value(1)
        self.tree.add_value(0)
        self.tree.add_value(2)
        self.tree.add_value(8)
        self.tree.add_value(5)

    def test_count(self):
        self.assertEqual(self.tree.get_count(), 10)

    def test_sum(self):
        self.assertEqual(self.tree.get_sum(), 38)

    def test_avg(self):
        self.assertEqual(self.tree.get_avg(), 3.8)

    def test_median(self):
        self.assertEqual(self.tree.get_median(), 4)

if __name__ == '__main__':
    unittest.main()