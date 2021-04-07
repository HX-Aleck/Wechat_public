'''
    模块化与参数化通常需要配合使用，即在创建函数和类方法时为它们设置入参，从而使它们可以根据不同的参数
执行相应的操作。
    假设要实现一个关于邮箱的自动化测试项目，那么可能每条测试用例都需要有登陆和退出，此时用一个module.py
文件存放登陆和退出动作。
'''
from selenium import webdriver
from time import sleep
from Selenium.module import Mail


Chrome_driver = 'C:\Program Files\Driver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=Chrome_driver)
driver.get('https://mail.163.com/')

mail = Mail(driver)
# 登陆账号密码
mail.login('1876。。。。', 'a。。。。。')
sleep(5)
mail.logout()

driver.quit()


