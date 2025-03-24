# 输入一个整数n，判断该数是否为完数。所谓完数(Perfect number)，是一些特殊的自然数，它所有的真因子(即除了自身以外的约数)的和，恰好等于它本身。比如6=1+2+3，所以6是完数。
# 输入输出格式：
# 输入：一行，表示整数n
# 输出：一行，表示判断结果（是完数或者不是完数）
# 输入输出样例1：
# 5
# 不是完数
# 输入输出样例2：
# 6
# 是完数

yueshu = []
num = int(input())
for i in range(1,num):
    if num % i == 0:
        yueshu.append(i)
if num == sum(yueshu):
    print("是完数")
else:
    print("不是完数")
