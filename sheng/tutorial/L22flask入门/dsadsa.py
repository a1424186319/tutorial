import time
def foo4():
    # \r 表示光标回到行首  # \n 光标先回到行首，再往下一行。
    for i in range(101):
        time.sleep(0.01)
        print("\r Loading...{}% ".format(i), end="")
foo4()

