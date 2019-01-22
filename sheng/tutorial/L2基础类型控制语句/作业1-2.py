passed = ''
rank = ''
score = input('请输入成绩：')
score = float(score)
if 0 <= score < 60:
    passed = '不及格'
elif 60 <= score <= 100:
    passed = '及格'
    if 60 <= score < 70:
        rank = '等级D'
    elif 70 <= score < 80:
        rank = '等级C'
    elif 80 <= score < 90:
        rank = '等级B'
    elif 90 <= score <= 100:
        rank = '等级A'
else:
    print('成绩输入错误')
print(passed)
print(rank)

# #用户输入
# score = input('请输入学生成绩：')
# score = int(score)
# #print(score,type(score))
#
# #判断成绩
# if score < 0 or score >100:
#     print('用户输入不合法')
# else:
#     #输入合法
#     if 0 <= score < 60:
#         print('不及格')
#     else:
#         print('及格')
#         if 60 <= score < 70:
#             print('D')
#         elif 70 <= score < 80:
#             print('c')
#         elif 80 <= score < 90:
#             print('B')
#         elif 90 <= score <= 100:
#             print('A')
