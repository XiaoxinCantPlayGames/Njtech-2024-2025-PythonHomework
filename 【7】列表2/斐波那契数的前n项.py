# 斐波那契数列又称黄金分割数列、兔子数列，其第1、2项均为1，从第3项开始每一项都是前两项之和，即1，1，2，3，5，8，13，21，34，……。试编写程序，利用列表计算斐波那契数列前n项。并将列表输出。n(n>=2)由用户输入。
# 样例：
# 输入：
# 10
# 输出：
# [1,1,2,3,5,8,13,21,34,55]


# 直接切片打印结果：需要注意切片的左闭右开
n = int(input())
x, y, count = 1, 1, 2 # x和y是数列中的第一二项，count是用来计数的
_ = [] # 存放计算结果的列表
_.append(x)
_.append(y)
while count < n: # 判断现在计算的项够不够输出的n项
    x = x + y
    y = x + y
    _.append(x)
    _.append(y)
    count += 2 # 经过一次循环，计算出了数列中的下面两项，所以用来count计数需要加2
print(_[:n+1]) # 直接切片打印结果


# 转存列表：不需要考虑切片的左闭右开
n = int(input())
x, y, count = 1, 1, 2 # x和y是数列中的第一二项，count是用来计数的
_ = [] # 用于存放计算结果的临时列表
result = [] # 这个才是存放结果的列表
_.append(x)
_.append(y)
while count < n: # 判断现在计算的项够不够输出的n项
    x = x + y
    y = x + y
    _.append(x)
    _.append(y)
    count += 2 # 经过一次循环，计算出了数列中的下面两项，所以用来count计数需要加2
for i in range(n): # 将运算结果转存到答案中
    result.append(_[i])
print(result)


