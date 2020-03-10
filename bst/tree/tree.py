from .node import Node

class Tree:
    def __init__(self):
        self.root = None

    def __str__(self):
        return str(self.root)

    def get_levels(self):
        return self.root.get_levels()
    
    def find(self, value):
        if self.root:
            return self.root.find(value)

    def add_value(self, value):
        if not self.root:
            self.root = Node(value)
            return self.root
        else:
            self.root.add_value(value)

    def get_count(self):
        if self.root:
            return self.root.get_count()
        return 0
    
    def get_avg(self):
        if self.root:
            return self.root.get_avg()
    
    def get_inorder_traversal(self):
        if self.root:
            return self.root.get_inorder_traversal()
    
    def get_median(self):
        traversal = self.get_inorder_traversal()
        traversal_len = len(traversal)
        if traversal_len % 2:
            return traversal[(traversal_len - 1) // 2]
        return (traversal[traversal_len // 2 - 1] + traversal[traversal_len // 2]) / 2

    def get_sum(self):
        if self.root:
            return self.root.get_sum()
        return 0
