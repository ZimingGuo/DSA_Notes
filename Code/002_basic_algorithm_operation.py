# author: Ziming Guo
# time: 2020/8/17

#  python 中算法的优越性的问题

from timeit import Timer

#  timeit 测试模块，python 提供的

# python 中对列表进行添加数据的操作：
# lst = []
# lst.append(1)  # 这句不算是基本步骤，因此时间复杂度不能是 1 了
# lst.insert(1)
#  基本步骤指的是不会进行函数调用的，函数是对基本步骤的封装
#  实际上 append 和 insert 也是有优劣之分的，执行的速度也是不同的


# 测算一下在构造列表的时候的几种可能性
lst01 = [1, 2]
lst02 = [23, 5]

# 加操作
lst03 = lst01 + lst02

# 列表生成器
lst04 = [i for i in range(10000)]

# 把可迭代对象直接转换成列表
lst05 = list(range(10000))
# python2 中的 range 直接返回的是一个列表对象；python3 中的 range 返回的是一个可迭代对象

# 往空列表当中追加元素
lst06 = []
for i in range(10000):
    lst06.append(i)


# 进行测试：
# 测试直接追加操作
def test01():
    list01 = []
    for i in range(10000):
        list01.append(i)


# 测试列表相加
def test02():
    list02 = []
    for i in range(10000):
        # list02 += [i]
        list02 = list02 + [i]


# 测试列表生成器
def test03():
    list03 = [i for i in range(10000)]


# 测试可迭代对象直接转换
def test04():
    list04 = list(range(10000))


# 测试 extend 的方式增加列表元素
def test05():
    list05 = []
    for i in range(10000):
        list05.extend([i])


# 测试 insert 的方式向列表中加元素
def test06():
    list06 = []
    for i in range(10000):
        list06.insert(0, i)  # 表示向列表头中加元素


# 构造一个 timer 测算器类用于对执行时间进行测算，timer 是一个类的形式
timer01 = Timer("test01()", "from __main__ import test01")
"""
第一个参数应该为执行的语句，此参数应该是一个字符串形式的函数名，而不是函数；因此加上引号，代表对应的函数
第二个参数表示进行设置：即从当前的 002 文件中导入 test01
然后这个测算器就构造好了
"""
# 运行测算器，执行一千次（逐个 append）
print("+:", timer01.timeit(1000))  # 会返回时间，单位是秒，可以直接打印

# （列表相加）
timer02 = Timer("test02()", "from __main__ import test02")
print("列表相加（一个一个直接加）:", timer02.timeit(1000))

# 列表生成器
timer03 = Timer("test03()", "from __main__ import test03")
print("[i for i in range()]:", timer03.timeit(1000))

# 用可迭代对象直接转换
timer04 = Timer("test04()", "from __main__ import test04")
print("list(range()):", timer04.timeit(1000))

# 测试 extend 的方式增加列表元素
timer05 = Timer("test05()", "from __main__ import test05")
print("extend:", timer05.timeit(1000))

# 测试 insert 的方式怎加列表元素
timer06 = Timer("test06()", "from __main__ import test06")
print("insert:", timer06.timeit(1000))

# 第一个参数代表要执行的代码，第二个参数表示执行的过程中需要调的包

"""
结果分析：
    效率排序：可迭代对象 > 列表生成器 > append > 列表相加 > extend > insert向队头添加
    列表相加 & extend 比较：列表相加每次都会生成一个新的列表；extend 每次只是向原来的列表增加一个元素，不会生成一个新的列表
    append & extend：append 里面加的必须是一个元素；extend 里面是一列表
    append & insert：append 是向列表尾部添加；insert向指定位置加入元素
    tips：向列表头添加元素要比向列表尾部添加元素效率低得多
    
    list 和 dict 实际上是不能算作基本数据类型的，因为 list 和 dict 都是python已经帮我们封装好的
    
    需要知道的：
    1) 索引是 O(1)
    2) 队尾添加是 O(1)
    3) 在任意位置 pop 和 insert 是 O(n)
    4) 查找是 O(n) 
    
    list += [i] 和 list = list + [i] 不同，前者不会生成一个新列表，是在原列表上进行操作；后者是每次都会生成一个新的列表
    list = list + [i] 这种直接列表相加的方式效率很低很低
"""
