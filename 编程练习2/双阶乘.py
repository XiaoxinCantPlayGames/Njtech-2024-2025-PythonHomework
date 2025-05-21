# 2. (程序题) 一个正整数的双阶乘，表示不超过这个正整数且与它有相同奇偶性的所有正整数乘积。
# n 的双阶乘用 n!! 表示。
# 例如：
# 3!! = 3 × 1 = 3。
# 8!! = 8 × 6 × 4 × 2 = 384。
# 11!! = 11 × 9 × 7 × 5 × 3 × 1 = 10395。
# 请问，2021!! 的最后 5 位（这里指十进制位）是多少？
# 要求：定义一个函数 fun()，用来求出某个正整数的双阶乘。
# 主程序输出格式：一个值，表示2021!! 的最后 5 位数。



# 函数
def fun(num):
    result = 1
    for i in range(num+1):
        if i % 2 == num % 2: # 用来判断奇偶性是不是和给的数字一样
            result *= i
    return result

print(str(fun(2021))[-5:])

# 由于本题是知道要算的数是什么，因此在函数编写的时候就可以带入实际的数字，这个时候形参就可以不用写了
def fun():
    result = 1
    for i in range(2022):
        if i % 2 == 2021 % 2: # 用来判断奇偶性是不是和给的数字一样
            result *= i
    return result    
print(str(fun())[-5:])

# 循环
result = 1
for i in range(2022):
    if i % 2 == 2021 % 2:
        result *= i
print(str(result)[-5:])


# 很显然这道题可以当一个填空题，知道答案就可以了
print(59375)


# 实在写不出来的同学，可以用random库随机一个答案
import random
n = random.randint(59375,59376) # 一定要赋值到一个变量上面再打印，直接打印会报错
print(n)