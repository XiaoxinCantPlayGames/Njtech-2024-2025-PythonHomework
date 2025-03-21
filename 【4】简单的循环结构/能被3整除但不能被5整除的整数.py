# 输出1-n内所有能被3整除但不能被5整除的整数。n的值由用户输入。

n = eval(input())
d = 0
for i in range(1,n+1):
    if i % 3 == 0 and i % 5 != 0:
        print(i,end=" ")
        d += 1
        if d % 3 == 0:
            print()
