# 假设字典dic_country存储了部分国家的国家名与首都名的对应关系，其中国家名为键，首都名为值。试编写程序，根据用户输入的国家名查询首都名，如果存在则输出查询结果，否则提示“未查询到该国家名”。假设对国家名进行查询时不区分大小写。
# 字典内容：{"China":"Beijing","America":"Washington","Norway":"Oslo","Japan":"Tokyo","Germany":"Berlin","Canada":"Ottawa","France":"Paris","Thailand":"Bangkok"}
# 样例1：
# 输入：
# China
# 输出：
# Beijing
# 样例2：
# 输入：
# Austrilia
# 输出：
# 未查询到该国家名


dt = {"China":"Beijing","America":"Washington","Norway":"Oslo","Japan":"Tokyo","Germany":"Berlin","Canada":"Ottawa","France":"Paris","Thailand":"Bangkok"}
country = input()
print(dt.get(country,"未查询到该国家名"))  #获取输入国家的“值”，没有查询到就返回"未查询到该国家名"