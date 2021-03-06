# author: Ziming Guo
# time: 2020/8/19

# 将节点抽象出来，封装成一个类，而不是用 python 中的特殊数据类型(元组 etc)，具有普遍性
# 有一个节点，就应该构造一个节点对象，节点对象包括自身的数据和他的下一个节点的地址
# 创建两个类，一个是节点类，一个是链表类

class Node(object):
    """节点"""

    # init 初始化
    def __init__(self, elem):
        self.elem = elem  # 节点中有个区域专门用来保存数据
        self.next = None  # 一开始不知道节点的地址区应该指向谁，因此就指向空


class SingleLinkList(object):
    """单链表"""

    # 每一个对象函数都应该考虑到一个特殊情况：空列表
    # 存在一个属性，指向第一个节点，此属性应该是一个对象属性，即 每创建一个对象都要拥有这个属性
    # 且这个属性只是对这个类内部使用，不需要外部对他进行操作
    # 如果创建链表对象的时候没有传入第一个节点对象，默认第一个节点数据为0
    def __init__(self, node=None):
        self.__head = node

    # 下面的方法都应该是具体的对象方法，而不是类方法，因为这些方法都是对具体的链表类的对象的操作
    def is_empty(self):
        """链表是否为空(不需要参数)"""  # 只要 _head 属性指向的是 None 就表示是一个空链表
        return self.__head is None

    def length(self):
        """链表长度(不需要参数)"""
        # cur 游标用来移动遍历节点，让 cur 置为头节点
        cur = self.__head
        # count 用来记录数量
        count = 0
        # 进行游标移动（循环实现）
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表(不需要参数)"""
        cur = self.__head
        while cur is not None:
            print(cur.elem, end=" ")
            cur = cur.next
        print("")

    def add(self, item):
        """链表头部添加元素"""
        # 存在顺序问题，(1)先让新节点的 next 指向原链表的第一个节点的 elem，(2)然后再让原链表的头部指向新节点的 elem。否则原链表会丢失
        node = Node(item)  # 将 item 分装成一个节点
        node.next = self.__head
        self.__head = node

    def append(self, item):
        """链表尾部添加元素"""
        # item 不是一个节点，为而是下一个节点的具体元素内容，不用关心如何操作，只把数据给进来，自动封装成一点加到链表
        node = Node(item)
        if self.is_empty():  # 首先判断一个链表是否为空
            self.__head = node
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        """指定位置添加元素
        :param pos下标 从零开始
        """
        # 还是要注意顺序问题，即先让新节点 next 指向原链表后半段，再让原链表前半段指向新节点的 elem，防止丢失
        if pos <= 0:
            self.add(item)  # 在此链表中头添加
        elif pos > self.length() - 1:
            self.append(item)  # 在此链表中尾添加
        else:
            node = Node(item)
            pre = self.__head
            count = 0
            while count < (pos - 1):
                count += 1
                pre = pre.next
            # 当循环退出后 pre 指向 pos-1 的位置
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        """删除节点"""
        # 删除第一次出现的元素
        # 用两个游标实现 cur pre
        cur = self.__head
        pre = None
        while cur is not None:
            if cur.elem == item:
                # 判断当前节点是否是头节点
                # 头节点：pre = None
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def search(self, item):
        """查找节点是否存在"""
        cur = self.__head
        while cur is None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False  # 整个循环都没找到，表示没有此元素


# 测试代码：
if __name__ == "__main__":
    ll = SingleLinkList()  # 创建链表对象，先不传节点
    print(ll.is_empty())
    print(ll.length())

    ll.append(1)
    print(ll.is_empty())
    print(ll.length())

    ll.append(2)
    ll.add(8)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    # 8 1 2 3 4 5 6

    ll.insert(-2, 9)
    # 9 8 1 2 3 4 5 6

    ll.travel()
    ll.remove(9)
    ll.remove(6)

    ll.travel()
