class Node:
    def __init__(self):
        self.__parent = None
        self.__left = None
        self.__right = None
        self.__value = None
        self.__sum = 0
        self.__count = 0
        self.__current_median = None
        self.__median_value_before = None
        self.__median_value_after = None

    def __add_to_sum(self, value):
        if self.__parent:
            self.__parent.__add_to_sum()
        self.__sum += value
    
    def __sub_from_sum(self, value):
        if self.__parent:
            self.__parent.__sub_from_sum(value)
        self.__sum -= value

    def get_sum(self):
        return self.__sum

    def __add_to_count(self):
        if self.__parent:
            self.__parent.__add_to_count()
        self.__count += 1
    
    def __sub_from_count(self):
        if self.__parent:
            self.__parent.__sub_from_count()
        self.__count -= 1

    def get_count(self):
        return self.__count

    def get_avg(self):
        if self.__count:
            return self.__sum / self.__count
        return None

    def set_value(self, value):
        old_value = self.__value
        # if updating
        if old_value or old_value == 0:
            self.__sub_from_sum(old_value)
        # if new
        else:
            self.__add_to_count()

        self.__value = value

        self.__add_to_sum(value)

    def __update_node(self, node):
        self.__count += node.__count
        self.__sum += node.__sum

        node.__parent = self

    def set_left_node(self, node):
        if self.__left:
            self.__left.__parent = None
        self.__left = node
        self.__update_node(node)

    def set_right_node(self, node):
        if self.__right:
            self.__right.__parent = None
        self.__right = node
        self.__update_node(node)

    def __print(self, space=0):
        space += 10
        ret = ''
        if self.__right:
            ret += self.__right.__print(space)
        ret += "\n"
        ret += " " * (space - 10)
        if self.__value is None:
            ret += 'X'
        else:
            ret += str(self.__value)
        if self.__left:
            ret += self.__left.__print(space)
        return ret

    def __str__(self):
        return self.__print()