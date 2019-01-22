from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome = webdriver.Chrome()

chrome.get('http://www.baidu.com')

search_ele = chrome.find_element_by_id('kw')
search_ele.send_keys('python')
search_btn = chrome.find_element_by_id('su')
search_btn.click()
# 拖动滚动条
for x in range(1, 10):
    time.sleep(1)
    j = x/10
    js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % j
    chrome.execute_script(js)

# 点击下一页
chrome.find_element_by_class_name('n').click()
# 打印内容
s = chrome.find_elements_by_class_name('container_s')

for i in s:
    a = i.text
    print(a)



# time.sleep(2)
# chrome.quit()
