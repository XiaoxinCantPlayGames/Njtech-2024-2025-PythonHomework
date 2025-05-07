# 定义函数f，计算密码强度。并输入调用函数表达式进行测试。
# 密码强度计算规则（满足其中一条，密码强度增加一级）：
# 1、有数字
# 2、有大写字母
# 3、有小写字母
# 4、位数不少于8位
# 样例：
# f("123Abc456")
# 输出：
# 密码强度4级


# 集合
def f(password):
    result = 0
    if set(password).isdisjoint("1234567890") == False:  # 集合的内容isdisjoint()方法：判断密码中存不存在后面参数中的内容，下同
        result += 1
    if set(password).isdisjoint(set("qwertyuiopasdfghjklzxcvbnm")) == False:
        result += 1
    if set(password).isdisjoint(set("QWERTYUIOPASDFGHJKLZXCVBNM")) == False:
        result += 1
    if len(password) >= 8:
        result += 1
    return result

# ord()函数
def f(password):
    level1, level2, level3, level4 = 0, 0, 0, 0 # 题目上的各要求初始化为0
    if len(password) >= 8: # 判断该密码长度不少于8位
        level4 = 1 
    for i in password:
        if ord(i) in range(48,58): # 判断该字符是不是数字
            level1 = 1
        elif ord(i) in range(97,123): # 判断该字符是不是小写字母
            level2 = 1
        elif ord(i) in range(65,91): # 判断该字符是不是大写字母
            level3 = 1
    result = level1+level2+level3+level4
    return result

# 输入输出
level = eval(input())
print(f"密码强度{level}级")
