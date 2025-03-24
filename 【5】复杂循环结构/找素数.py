# 输出范围[a,b]内的所有素数，要求每行输出7个，各数之间用一个空格分隔。
# 示例：
# 输入：
# 1,100
# 输出：
# 2 3 5 7 11 13 17 
# 19 23 29 31 37 41 43 
# 47 53 59 61 67 71 73 
# 79 83 89 97

a,b = input().split(",")
a, b = int(a), int(b)
count = 0 
for i in range(max(a,2),b+1):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        count += 1
        print(i,end=" ")
        if count % 7 == 0:
            print()