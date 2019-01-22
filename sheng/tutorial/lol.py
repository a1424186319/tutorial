import os,shutil,time
sw = os.listdir('D:/E/')
print(sw)
# os.remove('D:/E/wegame/lol/lol.exe')   #删除一个指定文件
lj = 'D:/E/wegame/lol'


def foo4():
    # \r 表示光标回到行首  # \n 光标先回到行首，再往下一行。
    for i in range(101):
        time.sleep(0.02)
        print("\r 扫描文件中...{}% ".format(i), end="")
foo4()
for parent,dirnames,filenames in os.walk(lj):
    for filename in filenames:
        print(filename)     #列出文件夹下所有的目录与文件
print('扫描成功!')

# list1 =os.listdir(lj)
# for i in range(0,len(list1)):
#     path = os.path.join(lj,list1[i])
#     if os.path.isfile(path):
#         os.remove(path)
#     elif os.path.isdir(path):
#         shutil.rmtree(path)
# print('删除成功.')      #删除文件及目录

