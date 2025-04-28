# 定义函数f，计算一个给定正整数的各位数字之和。输入函数调用语句进行测试。
# 样例：
# 输入：
# f(324)
# 输出：
# 324的各位数字之和是9


def f(num):
    global n # 声明一个全局变量，之后对这个全局变量进行赋值，这样函数结束后，这个变量也会存在于内存中且可以调用
    n = num
    sum = 0
    for i in str(num):
        sum += int(i)
    return sum

result = eval(input())
print(f"{n}的各位数字之和是{result}")
