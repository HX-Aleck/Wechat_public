# 此处以百度首页和账号注册页为例

import time
from selenium import webdriver


Chrome_driver = 'C:\Program Files\Driver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=Chrome_driver)
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")

# 获得百度搜索窗口句柄
search_windows = driver.current_window_handle

driver.find_element_by_link_text('登录').click()
driver.find_element_by_link_text("立即注册").click()


# 获得当前所有打开的窗口句柄
all_handles = driver.window_handles

# 进入注册窗口
for handle in all_handles:
    if handle != search_windows:
        driver.switch_to.window(handle)
        print(driver.title)
        driver.find_element_by_name("userName").send_keys('crazy_crab')
        driver.find_element_by_name("phone").send_keys('1770。。。')
        driver.find_element_by_id("TANGRAM__PSP_4__password").send_keys('a。。。')
        driver.find_element_by_id("TANGRAM__PSP_4__verifyCodeSend").click()
        keys = input('请输入验证码：')
        driver.find_element_by_name("verifyCode").send_keys(keys)
        driver.find_element_by_id("TANGRAM__PSP_4__isAgree").click()
        driver.find_element_by_id("TANGRAM__PSP_4__submit").click()

        time.sleep(2)
        # 关闭当前窗口
    #    driver.close()

#driver.switch_to.window(search_windows)
#print(driver.title)

# driver.quit()