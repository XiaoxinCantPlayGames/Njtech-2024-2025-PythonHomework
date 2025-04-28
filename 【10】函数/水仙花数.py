# 设计一个函数，判断指定的一个三位正整数是否为水仙花数，并调用该函数进行测试。要求如下：
# 函数名：isSxh
# 返回值：是水仙花数返回True，不是水仙花数返回False
# 样例1：
# 输入：
# isSxh(153)
# 输出：
# 153是水仙花数
# 样例2：
# 输入：
# isSxh(103)
# 输出：
# 103不是水仙花数


def isSxh(num):
    global n # 声明一个全局变量，之后对这个全局变量进行赋值，这样函数结束的时候，这个变量也会存在于内存中且可以调用
    n = num
    a = str(num)
    if num == int(a[0])**3 + int(a[1])**3 + int(a[2])**3:
        return True
    return False

Flag = eval(input())

if Flag:
    print(f"{n}是水仙花数")
else:
    print(f"{n}不是水仙花数")