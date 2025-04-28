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


def f(password):
    result = 0
    if set(password).isdisjoint("1234567890") == False:  # 集合：判断密码中存不存在后面参数中的内容，下同
        result += 1
    if set(password).isdisjoint(set("qwertyuiopasdfghjklzxcvbnm")) == False:
        result += 1
    if set(password).isdisjoint(set("QWERTYUIOPASDFGHJKLZXCVBNM")) == False:
        result += 1
    if len(password) >= 8:
        result += 1
    return result

level = eval(input())
print(f"密码强度{level}级")
