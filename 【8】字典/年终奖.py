# 年底了，某公司要发年终奖。列表lst_staff中存放了所有员工的名单，内容为["李梅","张富","付妍","赵诺","刘江"]。字典dic_award中存放了对公司有杰出贡献的员工名单及奖金金额，内容为{"张富":10000,"赵诺":15000}。试编写程序，输出指定员工的年终奖金额。
# 注：
# 1、不在字典中的员工按照5000元/人发放年终奖。
# 样例1：
# 输入：
# 张富
# 输出
# 10000
# 样例2：
# 输入：
# 张三
# 输出：
# 该员工不存在
# 样例3：
# 输入：
# 李梅
# 输出
# 5000


lst_staff = ["李梅","张富","付妍","赵诺","刘江"]
reward = {"张富":10000,"赵诺":15000}

# 分支结构
staff = input()
if staff in lst_staff:
    if staff in reward:
        print(reward[staff])
    else:
        print(5000)  # 不在奖品的字典里面的员工直接输出5000
else:
    print("该员工不存在")

# get()方法
staff = input()
if staff in lst_staff:
    reward.get(staff,5000)
else:
    print("该员工不存在")
