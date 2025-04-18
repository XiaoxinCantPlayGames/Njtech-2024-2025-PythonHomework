# 进制转换。输入一个二进制整数，输出它对应的十进制数值。转换规则为按位和权重展开求和。
# 例如，二进制数 
# 输入输出样例：
# 输入：
# 11010
# 输出：
# 26

# 暴力算法
num = input()
print(int(num,2))

# 正常解法
num = input()
result = 0
for i in range(len(num)):
    result += int(num[-(i+1)]) * (2**i)
print(result)
