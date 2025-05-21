# 求闭区间[low, high]中所有整数n，满足n*n的值的每一位数字互不相同。
# 比如在范围[2000, 2100]内满足条件的整数及其平方数如下：
# 2013 4052169
# 2027 4108729
# 2069 4280761
# 2095 4389025
# 要求：
# 1)编写一个函数isdiff(n)，用来判断参数n的各位数字是否互不相同，若互不相同，则返回True，否则返回False。
# 提示：可将n转换成字符串，然后在遍历字符串的过程中，使用字符串的count函数统计当前字符出现的次数，如果次数大于1，则表示该字符串出现了重复的数字，此时遍历也可以提前退出。
# 2)程序的
# 输入：第一行表示下限low，第二行表示上限high；
# 输出：满足条件的n和n*n，n与n*n之间隔一个空格。
# 输入输出样例：
# 2000
# 2100
# 2013 4052169
# 2027 4108729
# 2069 4280761
# 2095 4389025



# 函数
def isdiff(n):
    if len(set(str(n*n))) == len(str(n*n)): # 用集合里面的元素唯一性，可以直接滤去相同的数字，再和原来的数字比较长度
        return True
    else:
        return False

low = int(input())
high = int(input())
for i in range(low,high+1):
    if isdiff(i):
        print(i,i*i)

# 循环
low = int(input())
high = int(input())
for i in range(low,high+1):
    if len(set(str(i*i))) == len(str(i*i)):
        print(i,i*i)

# 第二种条件判断:字典计数后看长度，这里用的循环为例
low = int(input())
high = int(input())
for i in range(low,high+1):
    number = {}
    for n in str(i*i):
        number[n] = number.get(n,0) + 1 # 字典计数
    if len(number) == len(str(i*i)):
        print(i,i*i)