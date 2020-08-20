# author: Ziming Guo
# time: 2020/8/19

# 将节点抽象出来，封装成一个类，而不是用 python 中的特殊数据类型(元组 etc)，具有普遍性
# 有一个节点，就应该构造一个节点对象，节点对象包括自身的数据和他的下一个节点的地址


class Node(object):
    """节点"""

    # init 初始化
    def __init__(self, elem):
        self.elem = elem  # 节点中有个区域专门用来保存数据
        self.next = None  # 一开始不知道节点的地址区应该指向谁，因此就指向空


class SingleLinkList(object):
    """单链表"""

    # 存在一个属性，指向第一个节点，此属性应该是一个对象属性，即 每创建一个对象都要拥有这个属性
    # 且这个属性只是对这个类内部使用，不需要外部对他进行操作
    # 如果创建链表对象的时候没有传入第一个节点对象，默认第一个节点数据为0
    def __init__(self, node=None):
        self._head = node

    # 下面的方法都应该是具体的对象方法，而不是类方法
    # 因为这些方法都是对具体的链表类的对象的操作
    def is_empty(self):
        """链表是否为空(不需要参数)"""
        pass

    def length(self):
        """链表长度(不需要参数)"""
        pass

    def travel(self):
        """遍历整个链表(不需要参数)"""
        pass

    def add(self, item):
        """链表头部添加元素"""
        pass

    def append(self, item):
        """链表尾部添加元素"""
        pass

    def insert(self, pos, item):
        """指定位置添加元素"""
        pass

    def remove(self, item):
        """删除节点"""
        pass

    def search(self, item):
        """查找节点是否存在"""
        pass

    # 还应构造函数实现将节点对象挂在链表中
