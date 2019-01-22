import time
import csv
# 引入自动化
from selenium import webdriver
# 1创建一个浏览器对象
chrome = webdriver.Chrome()
# 2.打开淘宝首页
chrome.get('https://www.jd.com')
# 3.找到我们在网页中表示搜索框的关键字
search_ele = chrome.find_element_by_id('key')

search_ele.send_keys('笔记本电脑')
# 5.找到需要按下按钮的相对的值
search_btn = chrome.find_element_by_class_name('button')
search_btn.click()

for i in range(1,4):
    print('正在获取第{}页数据，请稍后...'.format(i))
    time.sleep(1)


    for x in range(1,4,2):
        time.sleep(0.001)
        j = x*0.089
        js  = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % j
        chrome.execute_script(js)

    # 8 在浏览器拖动后,去除数据.

    with open('JD.txt', 'a', newline='', encoding='utf-8')as f:

        shops = chrome.find_elements_by_class_name('gl-i-wrap')
        for shop in shops:
            a = shop.text

            f.write(a)


        try:
            chrome.find_element_by_class_name('pn-next').click()
        except Exception as e:
            print('没有下一页了！')
            break


chrome.quit()

