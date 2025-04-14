# 假设字典dic_score存放了某班所有学生某门课的成绩，姓名作为键，成绩作为值。试编写程序，按照成绩从高到低的顺序输出所有学生的姓名。
# 样例：
# 输入：
# {"李刚":93,"陈静":78,"张金柱":88,"赵启山":91,"李鑫":65,"黄宁":83}
# 李刚
# 赵启山
# 张金柱
# 黄宁
# 陈静
# 李鑫


dic_score = eval(input())
dic = dict(sorted(dic_score.items(),key=lambda item:item[1],reverse=True)) # 以字典中的值，从大到小排序，lambda为匿名函数，后面接排序的函数
for i in dic:
    print(i)

