# 编写程序，实现分段函数的计算，分段函数的取值如下表所示。

x = eval(input())
if x<0:
    print(0)
elif 0<=x<5:
    print(x)
elif 5<=x<10:
    print(3*x-5)
elif 10<=x<20:
    print(0.5*x-2)
elif x>=20:
    print(0)
