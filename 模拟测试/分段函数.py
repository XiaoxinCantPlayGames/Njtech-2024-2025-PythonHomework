# 编写程序，实现分段函数的计算，分段函数的取值如下表所示。
# 输入输出格式说明
# 输入：一行，代表x的值
# 输出：一行，代表y的值
# 输入输出样例1：
# 0
# 0
# 输入输出样例2：
# 5
# 10



x = eval(input())
if x < 0:
    print(0)
elif 0<=x<5:
    print(x)
elif 5<=x<10:
    print(3*x-5)
elif 10<=x<20:
    print(0.5*x-2)
else:
    print(0)

