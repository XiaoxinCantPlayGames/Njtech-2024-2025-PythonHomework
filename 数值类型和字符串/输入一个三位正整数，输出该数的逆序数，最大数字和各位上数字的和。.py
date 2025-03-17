# 输入一个三位正整数，输出该数的逆序数，最大数字和各位上数字的和。

x = input()
y = eval(x)
print(eval(x[::-1]))
print(max(int(x[0]),int(x[1]),int(x[2])))
print(int(x[0])+int(x[1])+int(x[2]))