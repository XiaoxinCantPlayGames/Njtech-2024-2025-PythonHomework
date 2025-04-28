# 定义函数f，实现将一个十进制正整数转换成二进制数的功能。
# 转换方法：将十进制正整数不断对2取整取余，最后将余数倒序排列，即为二进制数。例如：
# 样例：
# f(11)
# 输出：
# 1011


# bin()内置函数
def f(num):
    n = str(bin(num)) # 内置的十进制传换成二进制函数
    return n[2:]

# 题意算法
def f(num):
    flag = True
    number = []
    while flag:
        if num // 2 != 0:
            number.append(str(num%2))
            num = num // 2
        else:
            number.append(str(num%2))
            flag = False
    return "".join(number[::-1])


print(eval(input()))

