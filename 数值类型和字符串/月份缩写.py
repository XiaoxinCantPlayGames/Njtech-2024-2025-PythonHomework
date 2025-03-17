# 已知月份字符串为：months="JanFebMarAprMayJunJulAugSepOctNovDec"
# 用户输入一个整数，输出对应的月份缩写。

months={"1":"Jan","2":"Feb","3":"Mar","4":"Apr","5":"May",
        "6":"Jun","7":"Jul","8":"Aug","9":"Sep",
        "10":"Oct","11":"Nov","12":"Dec"}
x = input()
print(months[x])