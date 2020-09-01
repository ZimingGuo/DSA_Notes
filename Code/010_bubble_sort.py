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
        count = 0
        for i in range(0, n - 1 - j):
            # 控制每个大循环中走几次
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                count += 1
            if count == 0:
                return  # 全部退出
    # 改进前的情况下 时间复杂度：n*n次，即 O(n^2)
    # 提出一种改进的方式：如果遍历第一次的时候发现这个序列原本就是有序的，就不需要再走第二次了，直接退出
    # 改进之后的最优时间复杂度就是 n ，但是最坏时间复杂度没有变化


# 先判断如何从头走到尾，再想清楚从头走到尾这样的大循环走几次


if __name__ == "__main__":
    lst01 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    bubble_sort(lst01)
    print(lst01)
