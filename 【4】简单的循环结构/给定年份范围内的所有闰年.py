# 输出给定年份范围内的所有闰年。
# 输出格式要求：年份与年份之间用空格隔开，每行输出10个年份

a = eval(input())
b = eval(input())
d = 0
for i in range(a,b+1):
    if i % 4 == 0 and (i % 100 != 0 or i % 400 == 0):
        print(i,end=" ")
        d += 1
        if d % 10 == 0:
            print()