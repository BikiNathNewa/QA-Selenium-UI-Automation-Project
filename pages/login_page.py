#contains XPATH and functions regarding login page
from selenium.webdriver.common.by import By

class loginPage:
    def __init__(self,driver):
        self.driver = driver
        self.email_textbox = (By.ID, "username")
        self.password_textbox = (By.ID, "password")
        self.login_button = (By.XPATH,"/html/body/div[4]/div[2]/div[2]/form/div[5]/button")
        
    def email(self, email):   #inputs values in the email textbox of login page
        self.driver.find_element(*self.email_textbox).send_keys(email)

    def password(self, password):   #inputs valies in the password textbox of login page
        self.driver.find_element(*self.password_textbox).send_keys(password)  
    
    def click_login(self):   #clicks on the login button of the login page
        self.driver.find_element(*self.login_button).click()
