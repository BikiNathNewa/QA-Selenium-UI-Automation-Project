#contains XPATH and functions regarding searching
from selenium.webdriver.common.by import By
import time

class searchPage:
    def __init__(self,driver):
        self.driver = driver
        self.searchbar_textbox = (By.XPATH, "/html/body/header[1]/div[2]/div/div[1]/form/input[1]")
        self.searchbar_button = (By.XPATH, "/html/body/header[1]/div[2]/div/div[1]/form/input[3]")
        self.login_button = (By.XPATH,"/html/body/div[4]/div[2]/div[2]/form/div[5]/button")
        self.barcode_button = (By.XPATH, "/html/body/header[1]/div[2]/div/div[1]/form/a")
        
        #advanced search
        self.ad_author = (By.XPATH, "/html/body/div[4]/div[3]/form/fieldset[2]/div[2]/input")
        self.ad_subject = (By.XPATH, "/html/body/div[4]/div[3]/form/fieldset[2]/div[4]/input")
        self.ad_search_button = (By.XPATH, "/html/body/div[4]/div[3]/form/button")
        
    def searchbar(self, book_name):   #types in bookname and clicks search button on the search bar
        self.driver.find_element(*self.searchbar_textbox).send_keys(book_name)
        time.sleep(1)
        self.driver.find_element(*self.searchbar_button).click()
        
    def clearbar(self):   #clears the searchbar
        self.driver.find_element(*self.searchbar_textbox).clear()
    
    def clickby_href(self, href):   #looks for a displayed book via href element
        self.driver.find_element(By.CSS_SELECTOR, f"a[href='{href}']").click()
         
    def click_barcode(self):   #clicks on the search by barcode button
        self.driver.find_element(*self.barcode_button).click()
    
    def author(self, author):   #types in author textbox of advanced search
        self.driver.find_element(*self.ad_author).send_keys(author)
    
    def subject(self, subject):   #types in subject textbox of advanced search
        self.driver.find_element(*self.ad_subject).send_keys(subject)    
        
    def ad_search(self):   #clicks on the search button present on the bottom of the advanced search page 
        self.driver.find_element(*self.ad_search_button).click()
    
    
