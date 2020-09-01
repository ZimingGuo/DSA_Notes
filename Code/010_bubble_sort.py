# author: Ziming Guo
# time: 2020/9/1
# 实现冒泡排序

# 可以在顺序表中实现冒泡排序，也可以在链表中实现
# 链表中实现冒泡排序较复杂，不仅仅要交换数据，还要将链表的结构进行调整
# 然而顺序表的话就只交换数据就可以了

def bubble_sort(alist):
    """冒泡排序"""
    # 对表中每一个元素的索引进行操作 好于 对数据直接进行操作
    n = len(alist)
    for j in range(n - 1):
        # 控制走几个大循环
        for i in range(0, n - 1 - j):
            # 控制每个大循环中走几次
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]


if __name__ == "__main__":
    lst01 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    bubble_sort(lst01)
    print(lst01)
