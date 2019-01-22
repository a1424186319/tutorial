# list1 = ['小明', '小王', '小李', '小红', '小赵']
# list2 = []
# def f(list1):
#     for i in range(0，len(list1)):
#         if i % 2 == 1:
#             print(list1[i])
#             list2.append(list1[i])
#         else:       (可省略)
#             pass    (可省略)
#     return list2

# print(f(list1))
list1 = ['小明', '小王', '小李', '小红', '小赵']
list2 = []
def f(list1):
    for i in range(len(list1)):
            list2.append(list1[1::2])
    return list2[0]
print(f(list1))
