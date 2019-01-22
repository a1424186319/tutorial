
import time

from selenium import webdriver
# 1.打开浏览器

driver = webdriver.Chrome()
# 2.打开淘宝首页
driver.get('http://www.taobao.com')

# 3.休眠2秒，找到输入框，输入查找的内容:笔记本电脑
driver.find_element_by_id('q').send_keys('笔记本电脑')
# 4.找到搜索按钮，点击
driver.find_element_by_class_name('btn-search').click()

for a in range(1, 5):
    print('正在获取第{}页数据，请稍后...'.format(a))
    time.sleep(1)

    for x in range(2, 10, 2):
        # 计算滚动比例
        j = x / 10
        # 拼接js代码
        js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * {}'.format(j)
        # 执行js
        driver.execute_script(js)

        time.sleep(0.5)

    divs = driver.find_elements_by_class_name('info-cont')

    print(len(divs))

    # 找下一页
    try:
        driver.find_element_by_link_text('下一页').click()
    except Exception as e:
        print('没有下一页了！')
        break


# 退出浏览器
driver.quit()


