# 将列表a中的数据线性变换成指定数值范围内的数据，并存放到列表b中。假设列表a中元素的最大值为max_value，最小值为min_value。当指定b中数据的取值范围为[low , high ]时，将列表a中的元素a[i]线性变换为列表b中的元素b[i]的变换公式为：
# b[i]=low + (a[i] - min_value) * (high - low)/(max_value - min_value)
# 要求：
# # 1) 定义函数transfer(a, low, high)，返回转换后的列表b。列表b中的小数位数保留4位，可使用round函数进行四舍五入，如round(0.1891891, 4)的结果为0.1892。建议使用列表生成式生成列表b。
# 2  共三行。
# 第一行，列表格式的数值序列a；第二行，变换后数据的下限low；第三行，变换后数据的上限high。
# 输出格式：
# 一行，表示变换后的列表b。
# 输入输出样例:
# 输入：
# [98, 35, 38, 100, 92, 99, 45, 94, 100, 3]
# 0
# 1
# 输出：
# [0.9794, 0.3299, 0.3608, 1.0, 0.9175, 0.9897, 0.433, 0.9381, 1.0, 0.0]



# 函数
def transfer(a,low,high):
    b = [round(low + ((i - min(a))*(high - low))/(max(a) - min(a)),4) for i in a]
    return b

a = eval (input())
low = int(input())
high = int(input())

print(transfer(a,low,high))

# 直接输出
a = eval (input())
low = int(input())
high = int(input())
b = [round(low + ((i - min(a))*(high - low))/(max(a) - min(a)),4) for i in a]
print(b)