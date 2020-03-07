class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def get_sum(self):
        value = self.value
        if self.left:
            value += self.left.get_sum()
        if self.right:
            value += self.right.get_sum()
        return value

    def find(self, value):
        if value == self.value:
            return self

        if self.right and value > self.value:
            return self.right.find(value)
        
        if self.left and value < self.value:
            return self.left.find(value)

    def length(self):
        counter = 1
        if self.left:
            counter += self.left.length()
        if self.right:
            counter += self.right.length()
        return counter
    
    def __str__(self):
        return '{} <- {} -> {}'.format(self.left, self.value, self.right)
