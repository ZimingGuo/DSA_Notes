# author: Ziming Guo
# time: 2020/9/1

# 实现栈结构

class Stack(object):
    """实现栈的结构"""

    def __init__(self):
        self.__list = []

    def push(self, item):
        """添加一个新的元素item到栈顶"""
        self.__list.append(item)
        # 在尾部进行操作的好处：顺序表在尾部操作时时间复杂度 O(1)
        self.__list.insert(0, item)
        # 在头部的操作的时间复杂度是 O(n)

        # 如果使用单链表的方式实现栈的结构，就应该在头部进行插入
        # 在链表中实现头部插入的时间复杂度是 O(1) 在尾部插入数据的时间复杂度为 O(n) 因为需要逐个遍历

    def pop(self):
        """弹出栈顶元素"""
        return self.__list.pop()

    def peek(self):
        """返回栈顶元素"""
        if self.__list:
            return self.__list[-1]
        # 如果列表为空
        else:
            return None

    def is_empty(self):
        """判断栈是否为空"""
        return self.__list == []

    def size(self):
        """返回栈的元素个数"""
        return len(self.__list)


if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    s.push(6)
    s.push(7)
    s.push(8)

    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
