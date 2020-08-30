# author: Ziming Guo
# time: 2020/8/30

class Node(object):
    """定义结点"""

    def __init__(self, item):
        self.elem = item
        self.next = None
        self.prev = None


class DoubleLinkList(object):
    def __init__(self, node=None):
        """双链表"""
        self.__head = node

    def is_empty(self):
        """链表是否为空"""
        return self.__head is None

    def length(self):
        """链表长度"""
        # cur 表示游标，用来移动遍历结点
        cur = self.__head  # 首先让游标指向头节点
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        cur = self.__head
        while cur is not None:
            print(cur.elem, end=" ")
            cur = cur.next
        print("")

    def add(self, item):
        """链表头部添加"""
        node = Node(item)
        node.next = self.__head
        self.__head = node
        node.next.prev = node

    def append(self, item):
        """链表尾部添加"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next is not None:
                # 找到最后一个结点
                cur = cur.next
                cur.next = node
                node.prev = cur

    def insert(self, pos, item):
        """
        指定位置添加
        pos 表示插入结点的位置
        """
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:  # 找到指定位置进行插入
            node=Node(item)
            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node


    def remove(self, item):
        """删除节点"""

    def search(item):
        """查找节点是否存在"""


if __name__ == "__main__":
    dll = DoubleLinkList()
