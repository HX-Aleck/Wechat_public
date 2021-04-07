from selenium import webdriver


Chrome_driver = 'C:\Program Files\Driver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=Chrome_driver)
driver.get("http://www.baidu.com")

# cookie信息是以字典形式存放在列表中
cookie = driver.get_cookies()
print(cookie)


# 添加cookie

driver.add_cookie({'name': 'key-aaaaa', 'value': 'value-bbbbb'})

# 遍历指定的cookies
for cook in driver.get_cookies():
    print("%s -> %s" % (cook['name'], cook['value']))