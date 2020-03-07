class Node:
    def __init__(self, parent, value):
        self.parent = parent
        self.value = value
        self.left = None
        self.right = None
    
    def __str__(self):
        return '{}: {} <- {} -> {}'.format(self.parent, self.left, self.value, self.right)

    def get_sum(self):
        value = self.value
        if self.left:
            value += self.left.get_sum()
        if self.right:
            value += self.right.get_sum()
        return value