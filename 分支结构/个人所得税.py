# 按照如下的个人所得税计算公式，请编写程序计算个人应交的所得税（为简单起见，本题未采用实际应用中的分段计税方式）：tax=rate*(salary-1600)。
# 当 salary≤1600 时，rate=0；
# 当 1600 < salary≤2500 时，rate=5%；
# 当 2500 < salary≤3500 时，rate=10%；
# 当 3500 < salary≤4500 时，rate=15%；
# 当 salary > 4500 时，rate=20%。

salary = eval(input())
if salary<=1600:
    rate=0
elif 1600<salary<=2500:
    rate = 0.05
elif 2500<salary<=3500:
    rate = 0.1
elif 3500<salary<=4500:
    rate = 0.15
elif salary>4500:
    rate = 0.2
print(rate*(salary-1600))