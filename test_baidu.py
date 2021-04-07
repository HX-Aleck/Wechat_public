from selenium import webdriver

#Edge_driver = 'C:\Program Files\Driver\MicrosoftWebDriver.exe'
#driver = webdriver.Edge(executable_path=Edge_driver)
Chrome_driver = 'C:\Program Files\Driver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=Chrome_driver)
driver.get('http://www.baidu.com')

driver.find_element_by_id('kw').send_keys('杂货铺727python')
driver.find_element_by_id('su').click()

# 退出
# driver.quit()