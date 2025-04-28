# 设计一个函数，判断指定的一个正整数是否为素数，并调用该函数进行测试。要求如下：
# 函数名：isPrime
# 返回值：是素数返回True，不是素数返回False
# 样例1：
# 输入：
# isPrime(7)
# 输出：
# 7是素数
# 样例2：
# 输入：
# isPrime(6)
# 输出：
# 6不是素数


def isPrime(num):
    global n # 声明一个全局变量，之后对这个全局变量进行赋值，这样函数结束的时候，这个变量也会存在于内存中且可以调用
    n = num
    if num == 1:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
    else:
        return True
    
Flag = eval(input())

if Flag:
    print(f"{n}是素数")
else:
    print(f"{n}不是素数")