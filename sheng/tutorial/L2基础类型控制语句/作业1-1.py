# 练习一 计算BMI指数
# 1 用户输入

height = input('请输入身高（cm）:')
weight = input('请输入体重（kg）:')
height = float(height)
weight = float(weight)

# 2 计算BMI
BMI = weight / (height/100 * height/100)
print(BMI)

# 3 if判断
if BMI < 18.5 :
    print('体重偏轻')
elif 18.5<= BMI <23.9:
    print('体重正常')
elif 23.9 <= BMI < 32:
    print('体重偏重')
elif BMI >= 32 :
    print('体重超重')