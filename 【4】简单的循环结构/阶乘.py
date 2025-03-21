# 编程计算1*2*3*……*n的结果。n的值由用户输入。
n = eval(input())
result = 1
for i in range(1,n+1):
    result = result*i
print(result)
