# 假设列表lst_info存放了某单位每个员工的基本信息(包括姓名、性别和年龄)。试编写程序，实现将用户要求的员工信息从列表中删除，并将删除信息后的列表输出。
# 提示：
# （1）列表内容和需要删除的员工姓名由用户输入
# （2）员工姓名不存在，则输出“该员工不存在”
# 样例：
# 输入：
# [["李玉","男",25],["金忠","男",23],["刘妍","女",21],["莫心","女",24],["沈冲","男",28]]
# 金忠
# 输出：
# [["李玉","男",25],["刘妍","女",21],["莫心","女",24],["沈冲","男",28]]


lst_worker = eval(input())
name = input()
lst_name = []
for i in range(len(lst_worker)):
    lst_name.append(lst_worker[i][0]) # 将员工姓名添加进一个列表中
if name in lst_name: # 判断员工是否存在
    num = lst_name.index(name) # 获取该员工的下标索引值
    lst_worker.pop(num) # 开除员工！
    print(lst_worker)
else:
    print("该员工不存在")