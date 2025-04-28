# 输出给定范围内的孪生素数（值相差为2的两个素数称为孪生素数）。范围的起始值和终止值由用户输入。
# 样例：
# 输入：
# 1
# 10
# 输出：
# 3 5
# 5 7


def isPrime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    else:
        return True

a = eval(input())
b = eval(input())

for i in range(max(a,2),b+1): # max(a,2)直接排除掉a小于2的情况
    if isPrime(i) and isPrime(i+2) and i+2 <= b: 
        print(i,i+2,sep=" ")
    else:
        continue