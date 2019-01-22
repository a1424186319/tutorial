#列表生成式（语法糖）
# 需求1.得到一个列表[1,2,3,...20]
# 普通写法-
list1 = []
for i in range(1,21):
    list1.append(i)
print(list1)
# 生成式写法
print([i for i in range(1,21)])

# 语法[变量 循环表达式]，解释器会自动把每一次循环的变量作为一项插入到列表当中。

# 场景：适合比较简单的列表生成，不必刻意使用。
# 复杂一点的例子。循环表达式后面又跟了if表达式，只有当if条件为True，i才会加入列表。
# 1.print([i for i in range(1,21) if i%2==0 ])

# 2.[i*i for i in range(1,11)]
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#（了解）生成器
g = (x for x in range(1,5))
g.__next__()  #1
g.__next__()  #2

