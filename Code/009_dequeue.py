# author: Ziming Guo
# time: 2020/9/1
#  实现双端队列

class Dequeue(object):
    """双端队列 """

    def __int__(self):
        self.__list = []

    def add_front(self, item):
        """从队头加入一个item元素"""
        self.__list.insert(0, item)

    def add_rear(self, item):
        """从队尾加入一个item元素"""
        self.__list.append(item)

    def pop_front(self):
        """从队列头部取出一个元素"""
        return self.__list.pop(0)

    def pop_rear(self):
        """从队尾取出一个item元素"""
        return self.__list.pop()

    def is_empty(self):
        """判断双端队列是否为空"""
        return self.__list == []

    def size(self):
        """返回队列的大小"""
        return len(self.__list)


if __name__ == "__main__":
    d = Dequeue()
