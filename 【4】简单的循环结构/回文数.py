# 输出1-n内所有的回文数。n由用户输入。
# 提示：设m是一任意自然数。若将m的各位数字反向排列所得自然数m1与m相等，则称m为一回文数。例如，若m=1234321，则称m为一回文数；但若m=1234567，则m不是回文数。
# 输出格式要求：数与数之间用逗号隔开

# 暴力输出
n = eval(input())
print(1,end="")
for m in range(2,n+1):
    if str(m) == str(m)[::-1]:
        print(end=",")
        print(m,end="")

# join()方法
n = eval(input())
a = []
for m in range(2,n+1):
    if str(m) == str(m)[::-1]:
        a.append(str(m))
print(",".join(a))

