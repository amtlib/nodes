from .node import Node

class Tree:
    def __init__(self):
        self.root = None
    
    def find(self, value):
        if self.root:
            return self.root.find(value)

    def add_value(self, value):
        if not self.root:
            self.root = Node(value)
            return self.root
        else:
            self.root.add_value(value)

    def length(self):
        if self.root:
            return self.root.length()
        return 0

    def get_sum(self):
        if self.root:
            return self.root.get_sum()
        return 0