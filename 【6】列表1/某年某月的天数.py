# 编写程序，输出某年某月的天数，某年某月由用户数输入。
# 提示：
# （1）创建一个列表，依次存放当年每个月对应的天数。
# （2）需要考虑闰年的情况。
# 样例：
# 输入：
# 2024-2
# 输出：
# 29


# 第一种：平年闰年两个列表
month_ping = [31,28,31,30,31,30,31,31,30,31,30,31]
mouth_run = [31,29,31,30,31,30,31,31,30,31,30,31]
year = input()
i = int(year[0:4])
mouth = int(year[-2:].strip("-")) # 获取后两位，若为个位数除去前面的“-”
if i % 4 == 0 and (i % 100 != 0 or i % 400 == 0):
    print(mouth_run[mouth-1])
else:
    print(month_ping[mouth-1])

# 第二种：一个列表，闰年二月单独输出
month_year = [31,28,31,30,31,30,31,31,30,31,30,31]
year = input()
i = int(year[0:4])
mouth = int(year[-2:].strip("-")) # 获取后两位，若为个位数除去前面的“-”
if i % 4 == 0 and (i % 100 != 0 or i % 400 == 0) and mouth == 2: # 判断是不是查询闰年2月
    print(29)
else:
    print(month_year[mouth-1])