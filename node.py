class Node:
    def __init__(self, parent, value):
        self.parent = parent
        self.value = value
        self.left = None
        self.right = None
    
    def __str__(self):
        return '{}: {} <- {} -> {}'.format(self.parent, self.left, self.value, self.right)