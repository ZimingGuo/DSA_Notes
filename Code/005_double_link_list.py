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
            cur = self.__head
            count = 0
            while count < pos:
                count += 1
                cur = cur.next
            node = Node(item)
            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node

    def remove(self, item):
        """删除节点"""
        cur = self.__head
        while cur is not None:
            if cur.elem == item:
                # 找到了所要删除的元素所在结点
                if cur == self.__head:  # 如果所要删除的结点就是第一个结点
                    self.__head = cur.next
                    if cur.next is not None:  # 判断链表是否只有一个结点
                        cur.next.prev = None
                else:
                    cur.prev.next = cur.next
                    if cur.next:  # 判断是否是最后一个结点
                        cur.next.prev = cur.prev
                break
            else:
                cur = cur.next  # 继续向下移动

    def search(self, item):
        """查找节点是否存在"""
        cur = self.__head
        while cur is not None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
            return False


if __name__ == "__main__":
    ll = DoubleLinkList()
    print(ll.is_empty())
    print(ll.length())

    ll.append(99)
    print(ll.is_empty())
    print(ll.length())
    ll.travel()
    print("*******************************")

    ll.append(2)
    ll.add(8)
    ll.travel()
    
    print("*******************************")
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    # 8 1 2 3 4 5 6

    ll.insert(-2, 9)
    ll.travel()
    # 9 8 1 2 3 4 5 6

    ll.travel()
    ll.remove(9)
    ll.remove(6)

    ll.travel()
