from selenium import webdriver
import time
# 根据环境变量找到chromdriver.exe进而驱动Chrome.exe
browser = webdriver.Chrome()
browser.get('http://www.baidu.com')
time.sleep(2)
browser.quit()
