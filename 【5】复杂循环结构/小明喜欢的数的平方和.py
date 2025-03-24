# 小明对数位中含有0、2、3、6的整数很感兴趣，比如1到20这样的整数有2、3、6、10、12、13、16、20。请编写程序输出从1到n中（包含n），所有小明感兴趣的整数的平方和。
# 示例：
# 输入：
# 2022
# 输出：
# 2067356391

num = int(input())
sum = 0
for i in range(num+1):
    a = str(i)
    if "0" in a or "2" in a or "3" in a or "6" in a:
        sum += i*i
print(sum)