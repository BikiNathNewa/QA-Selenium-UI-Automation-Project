#contains XPATH and functions regarding reading a book
from selenium.webdriver.common.by import By

class readBook:
    def __init__(self,driver):
        self.driver = driver
        self.borrow_button = (By.XPATH, "/html/body/div[4]/div[2]/div[1]/div[2]/div/div/div[1]/div/div[4]/div/a")
        self.nextpage_button = (By.XPATH, "/html/body/div[1]/main/div[2]/div[1]/div[1]/div/ia-book-theater/div[2]/div/div[2]/div/nav/ul[2]/li[3]/button/div")
        self.return_button = (By.XPATH,"/html/body/div[1]/main/div[2]/div[1]/div[1]/div/ia-book-theater/div[1]/ia-book-actions//section/collapsible-action-group//div/section[1]/button[1]")
        
    def click_borrow(self):
        self.driver.find_element(*self.borrow_button).click()
        
    def nextpage(self):
        self.driver.find_element(*self.nextpage_button).click()
        
    def return_book(self):
        self.driver.find_element(*self.return_button).click()
        
    
    
