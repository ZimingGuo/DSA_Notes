# author: Ziming Guo
# time: 2020/8/30


class Node(object):
    """节点"""

    def __init__(self, item):
        self.elem = item
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
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next is not self.__head:
                cur = cur.next
            # 退出循环之后
            node.next = cur.next
            cur.next = node

    def insert(self, pos, item):
        """在指定位置插入元素"""
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            pre = self.__head
            count = 0
            while count < (pos - 1):
                count += 1
                pre = pre.next
            # 退出循环后
            node = Node(item)  # 建立新结点
            node.next = pre.next
            pre.next = node

    def search(self, item):
        """查找遍历的结点"""
        if self.__head is None:
            return False
        cur = self.__head
        while cur.next is not self.__head:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        # 退出循环表示 cur 指向尾结点，上面的 while 循环中是没有查看到尾结点的
        if cur.elem == item:
            return True
        return False

    def remove(self, item):
        """删除结点"""
        # 先查看链表是否为空，不做任何操作并返回
        if self.is_empty():
            return
        cur = self.__head
        pre = None
        while cur.next is not self.__head:
            if cur.elem == item:
                if cur == self.__head:  # 如果要删除的元素是头结点
                    # 先找尾结点
                    rear = self.__head  # 建立新的游标，让他指向尾结点
                    while rear.next is not self.__head:
                        rear = rear.next
                    # 退出循环表示找到了尾结点
                    self.__head = cur.next
                    rear.next = self.__head
                else:  # 如果要删除的元素是中间结点
                    pre.next = cur.next
                return  # 不能用 break 应该是 return
            else:  # 如果没有找到这个元素对应的结点，两个游标分别移动
                pre = cur
                cur = cur.next
        # 退出循环，表示 cur 指向尾结点
        if cur.elem == item:
            if cur == self.__head:  # 表示链表只有一个结点
                self.__head = None
            else:  # 表示链表有很多结点
                pre.next = cur.next


if __name__ == "__main__":
    ll = SingleLinkList()
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
