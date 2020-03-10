import unittest
from tree.node import Node


class TestNodeMethods(unittest.TestCase):

    def setUp(self):
        self.parent = Node(5)

        new_node1 = Node(3)
        
        new_node2 = Node(2)

        new_node3 = Node(5)
        new_node1.set_left_node(new_node2)
        new_node1.set_right_node(new_node3)

        self.parent.set_left_node(new_node1)

        new_node4 = Node(7)
        new_node4.set_left_node(Node(1))
        new_node5 = Node(0)
        new_node5.set_left_node(Node(2))
        new_node6 = Node(8)
        new_node6.set_right_node(Node(5))
        new_node5.set_right_node(new_node6)
        new_node4.set_right_node(new_node5)
        self.parent.set_right_node(new_node4)

    def test_count(self):
        self.assertEqual(self.parent.get_count(), 10)
    def test_sum(self):
        self.assertEqual(self.parent.get_sum(), 38)
    def test_avg(self):
        self.assertEqual(self.parent.get_avg(), 3.8)
    def test_median(self):
        self.assertEqual(self.parent.get_median(), 4)
    # def test_avg(self):
    #     self.assertEqual('foo'.upper(), 'FOO')

    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())

    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

if __name__ == '__main__':
    unittest.main()