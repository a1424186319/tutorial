from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
# 打开、退出浏览器，请求网页
# driver = webdriver.Chrome()
# driver.get('http://www.baidu.com')
# time.sleep(5)
# driver.quit()

# 打开本地html测试页面
# 无头模式
# chrome_options = Options()


browser = webdriver.Chrome()
browser.get('file:///D:/2index.html')
time.sleep(1)

# 1> （常用）根据id或name值查找标签，打印标签属性、文本
# 实质上也是先lxml转换成文档树。 类似xpath\bs\ js document.getElementById('')   document.getElementsByName('')
elemt = browser.find_element_by_id('element_id')
elemt2 = browser.find_element_by_name('element_id')
print(elemt)

# 2> 取标签中值、属性

print(elemt.text)       # 标签内容
print(elemt.get_attribute('id'))            # 取属性

# 3> （常用）给标签中输入文本    elemt_obj.inner_text='new text'
elemt.send_keys("自动填充一些内容")
time.sleep(2)

# 4> (了解)根据标签内容选择标签。单击元素
elemt = browser.find_element_by_link_text('find_element_by_link_text')
print(elemt.tag_name)   # 打印标签名
elemt.click()       # (常用） 鼠标单击
time.sleep(3)

# 5> (了解)根据css选择器语法查找标签
# 页面A 上链接打开了页面B，焦点在页面B，但不影响获取页面A元素。
elemt = browser.find_element_by_css_selector('.highlight')
elemt.send_keys('啦啦啦')
time.sleep(1)

# 6> (常用）根据xpath选择元素
elemt = browser.find_element_by_xpath('//*[@id="xpathname"]')
elemt.send_keys('根据xpath')
time.sleep(2)

# 7> 切换标签页。 获取网页源代码。
browser.switch_to.window(browser.window_handles[0])
print(browser.page_source)
time.sleep(2)

# 8> 切换到弹窗，点击确定
elemt = browser.find_element_by_tag_name('button')
elemt.click()
time.sleep(2)
browser.switch_to.alert.accept()

# 9> 跳转和回退
elemt = browser.find_element_by_link_text('forward_back')
elemt.click()
time.sleep(2)
browser.back()
time.sleep(1)
browser.forward()
time.sleep(1)

# 10>cookies
print(browser.get_cookies())
browser.add_cookie({'name':'test','domain':'www.baidu.com'})
print(browser.get_cookies())

# 11键盘特殊按键
# elemt.send_keys(Keys.RETURN)    #Keys.ENTER





browser.quit()