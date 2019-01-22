# 已知列表[1,2,3,4,5,1,3]，去重
# for循环  in 新建变量存储新列表。

#常规方法
list1 = [1,2,3,4,5,1,3]
list2 = []
for i in list1:
    if i not in list2:
        list2.append(i)
print(list2)

# list1 = list(set(list1))

# set 的方法,去掉重复的项后   再转成列表
# print(list(set(list1)))

list1 = [1,2,3,4,5,1,3]
list2 = []
for i in list1:
    if i not in list2:
        list2.append(i)
print(list2)
