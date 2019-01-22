# 多进程
from multiprocessing import Process
import os,time

def info(title):
    print(title)
    print('模块名',__name__)
    print('父进程',os.getpid())
    print('自己进程',os.getpid())
    print('\n\n')

def f(name):
    info('子进程')
    print('hello', name)

if __name__ == '__main__':
    info('主进程')
    p = Process(target=f, args=('bbb',))
    p.start()
    p.join()

# 每个进程Windows会分配唯一句柄，叫做pid,每个子进程是从父进程复制来的