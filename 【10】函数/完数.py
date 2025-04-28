# 设计一个函数，判断指定的一个正整数是否为完数，并调用该函数进行测试。要求如下：
# 函数名：isWs
# 返回值：是完数返回True，不是完数返回False
# 样例1：
# 输入：
# isWs(6)
# 输出：
# 6是完数
# 样例2：
# 输入： 
# isWs(7)
# 输出：
# 7不是完数


def isWs(num):
    global n # 声明一个全局变量，之后对这个全局变量进行赋值，这样函数结束的时候，这个变量也会存在于内存中且可以调用
    n = num
    yueshu = []
    for i in range(1,num):
        if num % i == 0:
            yueshu.append(i)
    if sum(yueshu) == num:
        return True
    return False

Flag = eval(input())


if Flag:
    print(f"{n}是完数")
else:
    print(f"{n}不是完数")