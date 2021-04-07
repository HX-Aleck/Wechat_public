from time import sleep
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
Chrome_driver = 'C:\Program Files\Driver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=Chrome_driver)
driver.get('http://www.baidu.com')

# 打开搜索设置

link = driver.find_element_by_id('s-usersetting-top').click()
driver.find_element_by_link_text("搜索设置").click()
sleep(2)

# 搜索结果显示条数
sel = driver.find_element_by_id("se-setting-3")
'''
# value = '20'，获取到的sel里面必须要有<select>元素，要不然以下就不能用
Select(sel).select_by_value("20")
sleep(2)

# <option>每页显示50条</option>
Select(sel).select_by_visible_text("每页50条")
sleep(2)

# 根据索引
Select(sel).select_by_index(0)
sleep(2)
'''
# 百度这首页中为下拉框在span里面，因此不能使用以上注释方法

sel.find_element_by_link_text("每页50条").click()
