# 编写程序，根据输入的百分制分数，将其转换为等级制（优、良、中、及格、不及格） 并输出，如果分数不在0-100范围内，则输出“输入有误”。转换规则如下所示：
# 分数 Score（百分制）    等级 Grade
# Score ≥ 90                 优
# 80 ≤ Score < 90         良
# 70 ≤ Score < 80         中
# 60 ≤ Score <70         及格
# Score < 60                 不及格

score = eval(input())
if score<0 or score >100:
    print("输入有误")
else:
    if score>=90:
        print("优")
    elif 80<=score<90:
        print("良")
    elif 70<=score<80:
        print("中")
    elif 60<=score<70:
        print("及格")
    else:
        print("不及格")