# 编写程序，运行后用户输入4位整数作为年份，判断其是否为闰年。
# 如果年份能被400整除，则为闰年；或者如果年份能被4整除但不能被100整除，也为闰年。
# 比如2000、2016年都是闰年，1900、2017年不是闰年。

year = int(input())
if year%400==0 or (year%100 != 0 and year%4==0):
    print(f"{year}年是闰年")
else:
    print(f"{year}年不是闰年")