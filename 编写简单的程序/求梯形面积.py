# 编写程序计算梯形的面积。（上底、下底和高均由用户依次输入，面积使用round函数保留1位小数）

a = eval(input())
b = eval(input())
h = eval(input())
s = (a+b)*h/2
print(round(s,1))
