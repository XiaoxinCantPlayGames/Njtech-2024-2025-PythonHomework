# 在主程序中输出1000以内所有的素数，且这些素数为回文数，即回文素数。
# 【要求】
# ①定义一个函数，该函数用来判断某个整数是否为素数，是素数则函数返回True，否则返回False。
# ②定义一个函数，该函数用来判断某个整数是否为回文数，是回文数则函数返回True，否则返回False。
# ③输出格式：一行输出5个回文素数，每个素数之间用一个空格分隔。


# 函数
def isPrime(num):
    """
    用于判断是否为素数
    """
    if num == 1:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
    else:
        return True
    
def isHws(num):
    """
    用于判断是否为回文数
    """
    if str(num) == str(num)[::-1]:
        return True
    return False

count = 0
for i in range(1,1001):
    if isHws(i) and isPrime(i):
        if count % 5 == 0 and count != 0:
            print()
        print(i,end=" ")
        count += 1


# 循环
count = 0
for i in range(1001):
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
        if str(i) == str(i)[::-1]: # 判断是质数后开始判断是不是回文数
            if count % 5 == 0 and count != 0:
                print()
            print(i,end=" ")
            count += 1

