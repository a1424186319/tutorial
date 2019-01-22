score = float(input('请输入成绩'))
if score < 0 or score > 100:
    print('输入不合法')
elif score < 60:
    print('F')
elif 60 <= score < 70:
    print('D')
elif 70 <= score < 80:
    print('C')
elif 80 <= score < 90:
    print('B')
elif score >= 90:
    print('A')
else:
    pass