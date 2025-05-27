# 素数，又称质数，是指除1和其自身之外，没有其他约数的正整数。例如2、3、5、13都是素数，而4、9、12、18则不是。特别地，规定1不是素数（因此自然数的质因数分解就是唯一的)。
# 如果一个数本身是素数，并且把最低位删除后得到的数仍是素数、再把最低位删除后得到的数仍是素数...如此往复，直到得到一个一位素数，我们就称它是“幸运素数”。以233为例：。233本身是素数；
# ·23=[233/10]是素数;
# ·2=[23/10|是素数，
# 因此233是“幸运”素数。而211则不是幸运素数：虽然211是素数，但21不是素数。请编程求出一定范围内的所有幸运数字。
# 输入输出示例：
# 输入
# 6
# 30
# 输出
# 7
# 23
# 29


# 判断素数函数
def isSushu(n):
    if n in (0,1):
        return 0
    for j in range(2,n):
        if n % j == 0:
            return 0 # 0等价于False
    else:
        return 1 # 1等价于True
    
# 输入
x = int(input())
y = int(input())

# 判断算法1（使用了try-except语句）
for i in range(x,y+1):
    try:
        if isSushu(i):
            num = i//10 # 地板除：目的除掉最后一位数
            while num >= 1:
                if isSushu(num):
                    num = num // 10
                    continue
                else:
                    raise # 生成一个错误，然后执行except的代码，使代码跳出两层循环
            print(i)
    except:
        continue

# 判断算法2（flag标记）
for i in range(x,y+1):
    flag = 0 # 用于标记是不是满足之后的条件
    if isSushu(i):
        num = i//10
        while num >= 1:
            if isSushu(num):
                num = num // 10 # 地板除：目的除掉最后一位数
                continue
            else:
                flag = 1 # 不满足则标记为1
                break
        if flag: # 标记为1，条件成立，break结束循环，这次循环的i不是幸运素数
            continue
        else:
            print(i)
