# 小明要为一条街的住户制作门牌号。这条街一共有n 位住户，门牌号从 1 到 n 编号。小明制作门牌的方法是先制作 0 到 9 这几个数字字符，最后根据需要将字符粘贴到门牌上，例如门牌 1017 需要依次粘贴字符 1、0、1、7，即需要 1 个字符 0，2 个字符 1，1 个字符 7。请问要制作所有的 1 到 n 号门牌，总共需要多少个字符 2？n由用户输入。
# 示例：
# 输入：
# 2020
# 输出：

n = int(input())
count = 0
for i in range(1,n+1):
    num = str(i)
    for j in num:
        if j == "2":
            count += 1
print(count)
