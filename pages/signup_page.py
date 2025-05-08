#contains XPATH and functions regarding signup page
from selenium.webdriver.common.by import By

class signupPage:
    def __init__(self,driver):
        self.driver = driver
        self.nav_signup = (By.XPATH, "/html/body/header[1]/ul[2]/li[2]/a")
        self.email_textbox = (By.ID, "emailAddr")
        self.username_textbox = (By.ID, "username")
        self.password_textbox = (By.ID, "password")
        self.signup_button = (By.ID,"signup")
        
        self.login_link = (By.XPATH, "/html/body/div[4]/div[2]/div[2]/form/div[5]/p/a")
        self.signup_link = ( By.XPATH, "/html/body/div[4]/div[2]/div[2]/form/p/a")
        
    def email(self, email):   #inputs values in the email textbox of signup page
        self.driver.find_element(*self.email_textbox).send_keys(email)
        
    def username(self, username):   #inputs values in the username textbox of signup page
        self.driver.find_element(*self.username_textbox).send_keys(username)

    def password(self, password):   #inputs values in the password textbox of signup page
        self.driver.find_element(*self.password_textbox).send_keys(password)  
    
    def signup(self):   #clicks on the signup button present on the navbar
        self.driver.find_element(*self.nav_signup).click()
    
    def click_signup(self):   #clicks on the signup button present in the sign up page
        self.driver.find_element(*self.signup_button).click()
        
    def click_login_link(self):   #clicks on the link present in the sign up page which redirects to the login page
        self.driver.find_element(*self.login_link).click()

    def click_signup_link(self):   #clicks on the link present in the login page which redirects to the sign up page
        self.driver.find_element(*self.signup_link).click()