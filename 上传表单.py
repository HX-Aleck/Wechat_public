import os
from selenium import webdriver


file_path = os.path.abspath('./')

Chrome_driver = 'C:\Program Files\Driver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=Chrome_driver)

upload_page = 'file:///' + file_path + '/upfile.html'
driver.get(upload_page)
print(file_path + '\\3D.jpg')
driver.find_element_by_id("inputfile").send_keys(file_path + '\\3D.jpg')