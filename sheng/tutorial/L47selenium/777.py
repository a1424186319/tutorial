from selenium import webdriver
from time import sleep

# 新建webdriver对象
driver = webdriver.Chrome()
driver.get('http://nkg.122.gov.cn/')


driver.find_element_by_xpath('//*[@id="meta-feathre"]/ul/li[2]/a').click()
sleep(15)
driver.find_element_by_xpath('//*[@id="indexIsAgree"]').click()
driver.find_element_by_xpath('//*[@id="test"]/div/div/div[2]/div/input[2]').click()


