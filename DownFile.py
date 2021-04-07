import os
from selenium import webdriver

options = webdriver.ChromeOptions()

# 设置查看webdriver.ChromeOptions()help文档
prefs = {'profile.default_content_settings.popups': 0,
         'download.default_directory': os.getcwd()}
options.add_experimental_option('prefs', prefs)

Chrome_driver = 'C:\Program Files\Driver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=Chrome_driver, chrome_options=options)
driver.get('https://pypi.org/project/selenium/#files')
driver.find_element_by_partial_link_text("selenium-3.141.0.tar.gz").click()