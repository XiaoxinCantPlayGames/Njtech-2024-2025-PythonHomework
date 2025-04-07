# 编写程序，使用列表存放n个学生的姓名和年龄，并将列表结果输出。n及学生的姓名和年龄由用户输入。
# 样例：
# 输入：
# 3
# 张三
# 18
# 李四
# 19
# 王二
# 20
# 输出：
# [['张三', 18], ['李四', 19], ['王二', 20]]


n = int(input())
lst_student = [] # 创建一个外层列表
for i in range(n):
    student = [] # 这个列表是要放进去的嵌套列表
    name = input()
    old = int(input())
    student.append(name)
    student.append(old)
    lst_student.append(student)
print(lst_student)