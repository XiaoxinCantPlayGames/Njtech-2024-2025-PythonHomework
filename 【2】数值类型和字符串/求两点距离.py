# 输入平面直角坐标系中的两点坐标 A(x1,y1) 和 B(x2,y2)。
# 计算AB两点之间的距离，结果保留两位小数。

import math

x1,y1 = eval(input())
x2,y2 = eval(input())
x = math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))

print(f"{x:.2f}")