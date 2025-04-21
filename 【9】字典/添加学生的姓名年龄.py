# 编写程序，实现以下功能：
# （1）先创建空字典 dic_student。
# （2）由用户依次输入五名学生的姓名和年龄（直接在代码中使用赋值语句增加条目，不需要使用input，具体值使用(3)中输出的数据），存入字典 dic_student。
# （3）输出字典 dic_student 中的内容，格式(姓名和年龄之间用一个空格分开)为
# 王建 18
# 张云 19
# 张秋雨 18
# 刘欢 17
# 姜宇 19


# 正常算法（按照题目的意思）
dic_student = {}
dic_student.update({"王建":"18"})
dic_student.update({"张云":"19"})
dic_student.update({"张秋雨":"18"})
dic_student.update({"刘欢":"17"})
dic_student.update({"姜宇":"19"})
items = dic_student.items()
for i in items:
    print(" ".join(i))

# 显然，这道题可以当填空题
print("王建 18\n张云 19\n张秋雨 18\n刘欢 17\n姜宇 19")