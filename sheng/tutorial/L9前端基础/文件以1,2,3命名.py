# 将一个文件夹中的所有文件夹以1,2,3命名
import os
path = 'D:/ToolsTemp/KeyboardTest'
def rename():
    file = os.listdir(path)
    i = 1
    for item in file:
        src = os.path.join(os.path.abspath(path), item)
        dst = os.path.join(os.path.abspath(path), str(i)+'.txt')  #后缀为.txt,可修改.
        os.rename(src, dst)
        i = i + 1
rename()
print('运行成功.')
# get_FileCreateTime()