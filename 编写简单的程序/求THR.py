# 生命在于运动。运动时心率（每分钟心跳的次数）必须达到靶心率（THR），才会产生明显的健身效果。THR可以从人的年龄计算出来。步骤如下；
#（1）计算最大心率：220-年龄；
#（2）计算THR：最大心率*60%（使用round函数将THR保留到整数）。
# 试编写程序计算某个人的THR，年龄由用户输入。

old = eval(input())
max_xin = 220 - old
THR = max_xin *0.6
print(round(THR))