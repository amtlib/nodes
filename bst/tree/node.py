class Node:
    def __init__(self, value):
        self.__value = value
        self.__left = None
        self.__right = None

    def get_sum(self):
        value = self.__value
        if self.__left:
            value += self.__left.get_sum()
        if self.__right:
            value += self.__right.get_sum()
        return value

    def find(self, value):
        if value == self.__value:
            return self

        if self.__right and value > self.__value:
            return self.__right.find(value)
        
        if self.__left and value < self.__value:
            return self.__left.find(value)

    def add_value(self, value):
        if value >= self.__value:
            if self.__right:
                self.__right.add_value(value)
            else:
                self.__right = Node(value)
                return self.__right
        else:
            if self.__left:
                self.__left.add_value(value)
            else:
                self.__left = Node(value)
                return self.__left

    def get_count(self):
        counter = 1
        if self.__left:
            counter += self.__left.get_count()
        if self.__right:
            counter += self.__right.get_count()
        return counter
    
    def get_levels(self):
        if self.__left:
            left_levels = self.__left.get_levels()
        else:
            left_levels = 0
        if self.__right:
            right_levels = self.__right.get_levels() if self.__left else 0
        else:
            right_levels = 0

        if left_levels > right_levels:
            return 1 + left_levels
        return 1 + right_levels

    def get_avg(self):
        return self.get_sum() / self.get_count()
    
    def get_inorder_traversal(self):
        res = []
        if self.__left:
            res.extend(self.__left.get_inorder_traversal())
        res.append(self.__value)
        if self.__right:
            res.extend(self.__right.get_inorder_traversal())
        return res
    
    def __print(self, space=0):
        space += 10
        ret = ''
        if self.__right:
            ret += self.__right.__print(space)
        ret += "\n"
        ret += " " * (space - 10)
        ret += str(self.__value)
        if self.__left:
            ret += self.__left.__print(space)
        return ret

    def __str__(self):
        return self.__print()
