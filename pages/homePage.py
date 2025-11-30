from selenium.webdriver.common.by import By

class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.username_textbox_id = "name"
        self.email_textbox_id = "email"
        self.phone_textbox_id = "phone"
        self.address_textbox_id = "textarea"
        self.welcome_link_class = "title"

    def enter_username(self, username):
        self.driver.find_element(By.ID, self.username_textbox_id).clear()
        self.driver.find_element(By.ID, self.username_textbox_id).send_keys(username)

    def enter_email(self, email):
        self.driver.find_element(By.ID, self.email_textbox_id).clear()
        self.driver.find_element(By.ID, self.email_textbox_id).send_keys(email)
    
    def enter_phone(self, phone):
        self.driver.find_element(By.ID, self.phone_textbox_id).clear()
        self.driver.find_element(By.ID, self.phone_textbox_id).send_keys(phone)

    def enter_address(self, address):
        self.driver.find_element(By.ID, self.address_textbox_id).clear()
        self.driver.find_element(By.ID, self.address_textbox_id).send_keys(address)