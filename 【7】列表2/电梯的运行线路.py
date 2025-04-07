# 假设已有列表lst_floor(内容由用户输入)，存放了某电梯在一段时间内经过的楼层。试编写程序，输出电梯的运行线路。符号"↑"表示上行一层，"↓"表示下行一层。
# 样例：
# 输入：
# [1,4,2,5,7,3]
# 输出：
# ↑↑↑↓↓↑↑↑↑↑↓↓↓↓


lst_floor = eval(input())
state = [] # 用于存放电梯经过怎么样的变换，上行还是下行
for i in range(len(lst_floor)-1):
    state.append(lst_floor[i+1]-lst_floor[i]) # 做差判断上行还是下行，并存放进列表中
for j in state:
    if j < 0: # 数值为负表示下行
        print(-j*"↓",end="") # 负数与字符串相乘无结果，需要转换为正数
    elif j > 0: # 数值为正表示下行
        print(j*"↑",end="")