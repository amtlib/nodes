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

    def length(self):
        if self.root:
            return self.root.length()
        return 0
    
    def avg(self):
        if self.root:
            return self.root.avg()

    def get_sum(self):
        if self.root:
            return self.root.get_sum()
        return 0