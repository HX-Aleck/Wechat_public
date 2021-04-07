# 本例展示多表单切换，进行自动登录163网易邮箱

from selenium import webdriver
from time import sleep

Chrome_driver = 'C:\Program Files\Driver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=Chrome_driver)
driver.get('https://mail.163.com/')
sleep(2)

login_frame = driver.find_element_by_css_selector('iframe[id^="x-URS-iframe"]')
driver.switch_to.frame(login_frame)
driver.find_element_by_name("email").send_keys("。。。@163.com")
driver.find_element_by_name("password").send_keys("。。。")
driver.find_element_by_id("dologin").click()
driver.switch_to.default_content()

#driver.quit()
