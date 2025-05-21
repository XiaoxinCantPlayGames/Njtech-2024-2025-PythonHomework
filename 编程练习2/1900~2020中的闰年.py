# 编写一个程序，在主程序中求1900~2020中所有的闰年，每行输出5个年份，每个年份用一个空格分隔。要求定义一个函数isLeap，该函数用来判断某年是否为闰年，是闰年则函数返回True，否则返回False。
# 判断闰年的方法：某年能被4整除但是不能被100整除，或者能被400整除。



# 函数
def isLeap(year):
    if year%400==0 or (year%100 != 0 and year%4==0):
        return True
    else:
        return False
    
count = 0 # 用来调整打印格式的计数
for year in range(1900,2021):
    if isLeap(year):
        if count % 5 == 0 and count > 1: # 当count=0时，与5做余数也为0
            print()
        print(f"{year}",end =" ")
        count += 1


# 循环
count = 0 # 用来调整打印格式的计数
for year in range(1900,2021):
    if year%400==0 or (year%100 != 0 and year%4==0):
        if count % 5 == 0 and count > 1: # 当count=0时，与5做余数也为0
            print()
        print(f"{year}",end =" ")
        count += 1


