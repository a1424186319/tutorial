#读本地文件-捕获异常版
try:
    file = open('chinese_utf8.txt','r',encoding='utf8')
    lines = file.readlines()
    print(lines)
    for line in lines:
        print(line.strip('\n'))
except FileNotFoundError as e:
    print('请检查路径和文件名')
except UnicodeDecodeError:
    print('检查编码方式是否正确')
except Exception as e:
    print(e)
finally:
    file.close()


FileNotFoundError
UnicodeDecodeError

"""
健壮：代码考虑了各种运行情况和出错情况，不容易出bug，代码完善，又称健壮。
"""