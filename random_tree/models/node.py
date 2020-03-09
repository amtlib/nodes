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
