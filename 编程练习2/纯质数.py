# 如果一个正整数只有 1 和它本身两个约数，则称为一个质数（又称素数）。前几个质数是： 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, · · · 。
# 如果一个正整数的所有十进制数位都是质数，我们称它为纯数。例如： 23是纯数，但是13不是纯数（因为1不是素数）。
# 如果一个正整数既是质数又是纯数，我们称它为纯质数。例如： 2,3, 5, 7, 23, 37 都是纯质数，而 11, 13, 17, 19, 29, 31 不是纯质数，当然 1, 4, 35也不是纯质数。请问，在 1 到 2023 （含2023）中，有多少个纯质数？
# 要求：
# ①定义一个函数 isPrime()，用来判断一个正整数是否为素数，是素数返回True，否则返回False。
# ②定义一个函数 isPure()，用来判断一个正整数是否为纯数，是纯数返回True，否则返回False。
# ③在主程序中调用上面两个函数，统计出1 到 2023中纯质数的个数。
# 输出格式：一个值，表示 1 到 2023 （含2023）中纯质数的个数。



# 函数
def isPrime(num):
    if num == 1 or num == 0:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
    else:
        return True
    
def isPure(num):
    """
    用来判断是否为纯数
    """
    for i in str(num):
        if not isPrime(int(i)):
            return False
    return True

Pure = [] # 你也可以用count+=1来计数，用列表只是为了便于查找错误
for n in range(2024):
    if isPrime(n) and isPure(n): # 判断纯质数
        Pure.append(n)
print(len(Pure))


# 由于个位非质数只有几个，纯质数可以直接用in判断
def isPure(num):
    """
    用来判断是否为纯数
    """
    for i in str(num):
        if i in (0,1,4,6,8,9):
            return False
    return True


# 循环算法
count = 0
for i in range(2024):
    flag = 0 # 用来判断是否要跳出外面的循环的条件
    if i == 1 or i == 0: # 用于排掉1和0，也可以再range()里面直接从2开始 
        continue
    for j in range(2,i):
        if i % j == 0:
            flag = 1
            break
    if flag: # 如果条件为1（特殊的布尔值）继续跳一层循环
        continue
    else:
        flag1 = 0 # 和上面的flag一个作用
        for x in str(i):
            if int(x) in (0,1,4,6,8,9):
                flag1 = 1
                break
        if flag1:
            continue
        else:
            count += 1
print(count)


# 当然也可以当成填空题
print(23)


# 实在不会做还是用random库随机数，至少感觉一个区间吧
import random
n = random.randint(1,100)
print(n)