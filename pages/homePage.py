from selenium.webdriver.common.by import By

class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.welcome_link_class = "app_logo"
        self.hamburger_menu_id = "react-burger-menu-btn"
        self.logout_link_linkText = "Logout"

    def click_welcome(self):
        self.driver.find_element(By.CLASS_NAME, self.welcome_link_class).click()

    def click_hamburger_menu(self):
        self.driver.find_element(By.ID, self.hamburger_menu_id).click()

    def click_logout(self):
        self.driver.find_element(By.LINK_TEXT, self.logout_link_linkText).click()