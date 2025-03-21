# 编写程序计算1*2*3 + 3*4*5 + 5*6*7 + ... +n*(n+1)*(n+2)的值
# n(n为奇数)的值由用户输入。
num = eval(input())
sum = 0
for i in range(1,num+1,2):
    sum = sum + i*(i+1)*(i+2)
print(sum)