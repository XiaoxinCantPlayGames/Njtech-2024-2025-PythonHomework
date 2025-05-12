# 给定一个列表 A1, A2, · · · , An。你可以从中选出两个数Ai 和 Aj ( i 不等于 j )，然后将Ai 和 Aj 一前一后拼成一个新的整数。例如 Ai 为 12 和 Aj  为 345 时可以拼成 12345 。注意交换 Ai 和 Aj 的顺序总是被视为 2 种拼法，即便是 Ai = Aj 时。请你计算有多少种拼法满足拼出的整数小于等于k。
# 提示：如何将12 和 345 拼成 12345 ？可使用 int(str(12)+str(345))，或者 int(f'{12}{345}')。
# 输入输出格式：
# 输入：一共两行，第一行为列表格式的数，第二行表示k。
# 输出：一个值，代表答案。
# 输入输出样例：
# [1,2,3,4]
# 33
# 输出：8
# 样例解释：上例产生的拼接的数分别为 12、13、14、21、23、24、31、32、34、41、42、43，一共12个，有8个比33小。



# count直接计数
num = eval(input())
k = int(input())
count = 0
for i in range(len(num)): 
    for j in range(len(num)): # for循环嵌套，满足“交换 Ai 和 Aj 的顺序总是被视为 2 种拼法”
        if i == j: # 当两个下标索引值相等时，即是同一个元素，跳过
            continue
        if int(str(num[i])+str(num[j])) < k:
            count += 1
print(count)


# 列表长度：方便查看程序判断了哪些数是对的，纠错比较方便
num = eval(input())
k = int(input())
ls = []
for i in range(len(num)):
    for j in range(len(num)):
        if i == j: 
            continue
        if int(str(num[i])+str(num[j])) < k:
            ls.append(int(str(num[i])+str(num[j])))
print(len(ls))