# 每个偶数（>=4）都能由两个素数相加得到。输出给定范围内（起始值大于2）每个偶数拆分成两个素数之和（具体格式见样例）的式子。
# 样例：
# 输入：
# 4
# 10
# 输出：
# 4=2+2
# 6=3+3
# 8=3+5
# 10=3+7


def isPrime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    else:
        return True

a = int(input())
b = int(input())

for i in range(max(a,4),b+1): # max(a,4)直接排除掉a小于4的情况
    if i % 2 == 0:
        for j in range(2,i):
            if isPrime(j) and isPrime(i-j): # 两数相加等于i，计算另外一个数是多少就用i减这个数
                print(f"{i}={j}+{i-j}")
                break
    else:
        continue