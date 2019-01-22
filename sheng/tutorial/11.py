def is_alphabet(uchar):
    """判断一个unicode是否是英文字母"""

    if (uchar >= '\u0041' and uchar <= '\u005a') or (uchar >= '\u0061' and uchar <= '\u007a'):

        return '英文'

    elif uchar >= '\u4e00' and uchar<='\u9fa5':

        return '中文'
    else:
        return '多捞哦'
a = input('请输入一个字符串')
print( is_alphabet(a))