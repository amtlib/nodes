class Node:
    def __init__(self, value=None):
        self.__parent = None
        self.__left = None
        self.__right = None
        self.__value = None
        self.__sum = 0
        self.__count = 0
        self.__median = None
        if value is not None:
            self.set_value(value)

    def get_value(self):
        return self.__value

    # sum
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

    # count
    def __add_to_count(self, count=None):
        if self.__parent:
            self.__parent.__add_to_count(count)
        if count != None:
            self.__count += count
        else:
            self.__count += 1
    
    def __sub_from_count(self):
        if self.__parent:
            self.__parent.__sub_from_count()
        self.__count -= 1

    def get_count(self):
        return self.__count

    # avg
    def get_avg(self):
        if self.__count:
            return self.__sum / self.__count
        return None

    # median
    def get_median(self):
        return self.__median

    def __get_values(self):
        values = []
        if self.__value is not None:
            values.append(self.__value)
        if self.__left:
            values.extend(self.__left.__get_values())
        if self.__right:
            values.extend(self.__right.__get_values())
        
        return values

    def __recalculate_median(self):
        if self.__parent:
            self.__parent.__recalculate_median()
        values = sorted(self.__get_values())
        if self.__count == 1:
            self.__median = values[0]
        elif self.__count % 2 == 0:
            self.__median = (values[int(self.__count / 2) - 1] + values[int(self.__count / 2)]) / 2
        else:
            self.__median = values[int(self.__count / 2)]

    # setting new value
    def set_value(self, value):
        old_value = self.__value
        # if updating
        if old_value or old_value == 0:
            self.__sub_from_sum(old_value)
            if value == None:
                self.__sub_from_count()
        # if new
        else:
            self.__add_to_count()
            # self.__median = value

        self.__value = value
        if self.__value != None:
            self.__add_to_sum(value)
        
        self.__recalculate_median()

    def __update_node(self, node):
        # self.__count += node.__count
        self.__add_to_count(node.__count)
        self.__sum += node.__sum
        self.__recalculate_median()

        node.__parent = self

    # setting new child
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

    # printing to the console
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
