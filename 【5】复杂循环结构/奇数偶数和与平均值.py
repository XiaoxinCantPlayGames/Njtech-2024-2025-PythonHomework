# 从键盘上输入若干个整数，并求出这些数中所有奇数之和、偶数之和及所有数的平均值。当从键盘输入字符'Q'或者'q'时，程序停止接收输入，并输出计算结果。
# 提示：使用while循环结构
# 输入输出格式说明：
# 输入：有多行，每行代表一个整数，最后一行为Q或者q。
# 输出：一行，依次为奇数之和、偶数之和、所有数的平均值，各值间隔一个空格。

jishu = 0 
oushu = 0
n = 0
while True:
    a = input()
    if a == "Q" or a == "q":
        break
    elif int(a) % 2 == 0:
        oushu += int(a)
    elif int(a) % 2 == 1:
        jishu += int(a)
    n += 1
if n == 0:
    print("未输入整数")
else:
    print(jishu,oushu,(jishu+oushu)/n)
