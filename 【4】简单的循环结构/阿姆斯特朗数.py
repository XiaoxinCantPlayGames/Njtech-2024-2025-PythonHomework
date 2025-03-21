# 输出符合要求的阿姆斯特朗数。
# 提示：如果一个n位正整数等于其各位数字的n次方之和,则称该数为阿姆斯特朗数。n由用户输入。

n = eval(input())
for i in range(10**(n-1),10**n):
    sum = 0
    for k in str(i):
        sum = int(k)**n + sum
    if sum == i:
        print(i,end=" ")