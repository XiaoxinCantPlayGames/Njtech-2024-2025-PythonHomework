# 输出n位整数中第一个能被9整除且个位数是5的数。n由用户输入。

n = int(input())
for i in range(10**(n-1),10**n):
    num = str(i)
    if i % 9 == 0 and num[-1] == "5":
        print(i)
        break