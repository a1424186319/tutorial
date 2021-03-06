#主题：控制语句，if语句


score = 101
if score < 0 or score > 100:
    print('分数不合法')
elif score < 60:
    print('不及格')
elif 60 <= score < 70:
    print('及格')
elif 70 <= score < 90:
    print('良')
elif score >= 90:
    print('优秀')
else:
    pass

"""if<条件>:
    条件为“True”或（非空的字符串，非空的列表，非0的整数）后执行的语句。
 关键字if判断条件，为True执行代码块中的语句，为False或（空字符串，空列表，0）的时候不执行。
 
 if<条件1>
    条件1为True执行的语句
 else：
    不满足上面条件时执行的语句
    
if<条件1>：
    ...
    elif<条件2>:
    ...
...

从上到下判断各个条件，如果走入一个分支，其它分支不会再走。设计项目需注意，怎么去设计，
注意控制语句的嵌套层数不要超过4层。
pass：不执行实际功能，只是为了占位置。
"""

#表达式就是一句代码。
#语句块：后面的代码是从属于前面的一个语句。
#     语法特点：一条语句，然后有一个冒号：，然后语句块以缩进（4个空格或一个tab）开始，     语句块有明显的层级关系。其他语言靠{}和；来区分。

#缩进：Python要求语句块强制缩进。必须为4个空格。tab和shift+tab调整代码缩进。
#缩进错误会报错，IndentationError: unex
# pected indent


# if 语句的单行写法
def get_max1(num1,num2):
#   if num1 > num2
#       return num1
#   else:
#       return num2
    return num1 if num1 > num2 else num2
print(get_max1(1,2))
print(get_max1(2,1))

# 类似三元表达式   c=a>b?1:0
# if else 语句块写成单行模式   return 返回值1 if 条件 else 返回值2，当if条件为True 返回返回值1，为False返回返回值2.