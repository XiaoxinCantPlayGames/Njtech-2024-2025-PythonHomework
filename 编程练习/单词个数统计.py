# 【单词个数统计】
# 输入一个英文字符串，编写程序，统计该字符串中不同英文单词的个数。（需要将,.替换为空格）
# 输入输出样例如下：
# 输入：
# A big black bear sat on a big black bug.
# 输出：
# 7



s=input()
s = s.replace(","," ") # 将,替换为空格
s = s.replace("."," ") # 将.替换为空格
s = s.lower()
lst = s.split()
dic = {} # 用字典来存放单词，顺便也可以计数
for word in lst:
    dic[word] = dic.get(word,0) + 1 
print(len(dic)) # 直接输出字典的长度就好了
