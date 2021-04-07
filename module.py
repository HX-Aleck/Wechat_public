class Mail:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        '''登陆'''
        login_frame = self.driver.find_element_by_css_selector('iframe[id^="x-URS-iframe"]')
        self.driver.switch_to.frame(login_frame)
        self.driver.find_element_by_name("email").send_keys(username + "@163.com")
        self.driver.find_element_by_name("password").send_keys(password)
        self.driver.find_element_by_id("dologin").click()

    def logout(self):
        self.driver.find_element_by_class_name("js-component-component ks1").click()