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


def isSushu(n):
    if n in (0,1):
        return 0
    for j in range(2,n):
        if n % j == 0:
            return 0
    else:
        return 1
    
x = int(input())
y = int(input())
for i in range(x,y+1):
    try:
        if isSushu(i):
            num = i//10
            while num >= 1:
                if isSushu(num):
                    num = num // 10
                    continue
                else:
                    raise
            print(i)
    except:
        continue
