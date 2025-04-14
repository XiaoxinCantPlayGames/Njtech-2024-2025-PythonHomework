# 试编写程序，统计给定的一段英文文本中出现频率最高的三个字母（按照频率从高到低排列）。
# 样例：
# 输入：
# In the future, China's medical system will shift its focus from basic digitalization to clinical digitalization that centers on patients, the report said.
# 输出：
# i
# t
# a

word = input()
word = word.lower() # 将字符串中的字母全部转换为小写
count = {}

for i in word:
    count[i]=count.get(i,0)+1 # 对字符串中出现的字符进行计数，并存在count这个字典中

dic = dict(sorted(count.items(),key=lambda item:item[1],reverse=True)) # 以字典中的值，从大到小排序，lambda为匿名函数，后面接排序的函数
a = 1 #用来计数，打印了个字符
for i in dic:
    if a > 3: # 如果已经打印了三个东西就结束
        break
    if i in ",./;'` ": # 出去标点和空格，进入下一个循环
        continue
    print(i)
    a += 1