# 求 s=a+aa+aaa+...+aaa...aaa的值，其中a是1~9之间的某个数字，n是一个正整数。例如:若a=2，n=5，则s=2+22+222+2222+22222=24690。要求定义一个函数fun()，该函数根据参数a和n的值返回表达式a+aa+aaa+...+aaa...aaa的值，并在主程序中测试该函数。
# 【要求】
# 1）程序运行时的
# 输入：必须是函数fun的调用表达式，比如fun(2, 5)；然后通过eval函数获取函数fun的返回值赋值给某个变量，形如 f = eval(input())。
# 输出：表达式的值。
# 2）输入输出样例：
# fun(2, 5)
# 24690



def fun(a,n):
    s = 0
    for i in range(1,n+1):
        s += int(str(a)*i)
    return s

print(eval(input()))

