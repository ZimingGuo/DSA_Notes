# author: Ziming Guo
# time: 2020/8/30


class Node(object):
    """节点"""

    def __init__(self, item, elem):
        self.elem = elem
        self.next = None


class SingleLinkList(object):
    """单向循环列表"""

    def __init__(self, node=None):
        self.__head = node
        # 如果传入的节点不为空，则实现回环（结点的next指向结点本身）
        if node:
            node.next = node

    def is_empty(self):
        """判断链表是否为空"""
        return self.__head is None

    def length(self):
        """链表长度"""
        if self.is_empty():  # 如果链表为空，长度就为0，之后不再执行
            return 0
        # 链表不为空就执行下面操作
        cur = self.__head
        count = 1
        while cur.next is not self.__head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        if self.is_empty():
            return
        cur = self.__head
        while cur.next is not self.__head:
            print(cur.elem, end=" ")
            cur = cur.next
        # 退出循环，cur 指向尾结点，但是尾结点的元素未打印
        print(cur.elem)

    def add(self, item):
        """链表头部插入元素"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next is not self.__head:
                cur = cur.next
            # 退出循环之后 cur 指向的就是尾结点
            node.next = self.__head
            self.__head = node
            cur.next = node

    def append(self, item):
        """尾部插入结点"""
        node = Node(item)
        