# 假设列表lst_student（内容由用户输入）存放了学生的基本信息（依次为学号、姓名和年龄）。试编写程序，根据用户输入的学生姓名查询其年龄并输出。如果姓名不存在，则输出"姓名有误"。
# 样例：
# 输入：
# [["001","李梅",19],["002","刘祥",20],["003","张武",18]]
# 刘祥
# 输出：
# 20


lst_student = eval(input())
lst_name = [] # 该列表用于存放学生姓名
for i in range(len(lst_student)):
    lst_name.append(lst_student[i][1])


name = input()
if name in lst_name: # 检查该姓名是否在学生中存在
    num = lst_name.index(name) # 获取关于该学生信息的列表的下标索引值
    print(lst_student[num][-1]) # 嵌套列表索引打印
else:
    print("姓名有误")

