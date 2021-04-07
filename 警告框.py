from time import sleep
from selenium import webdriver


Chrome_driver = 'C:\Program Files\Driver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=Chrome_driver)
driver.get('http://www.baidu.com')

# 打开搜索设置

link = driver.find_element_by_id('s-usersetting-top').click()
driver.find_element_by_link_text("搜索设置").click()
sleep(2)

# 保存设置
driver.find_element_by_class_name("prefpanelgo").click()

# 获取警告窗
alert = driver.switch_to.alert

# 获取警告窗提示信息
alert_text = alert.text
print(alert_text)

# 接受警告窗
alert.accept()


