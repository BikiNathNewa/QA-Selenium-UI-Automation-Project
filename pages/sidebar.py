#contains XPATH and functions regarding the sidebar
from selenium.webdriver.common.by import By
import time

class sidebarPage:
    def __init__(self,driver):
        self.driver = driver
        self.sidebar_button = (By.XPATH, "/html/body/header[1]/div[3]/details/summary/img[2]")
        #profile section
        self.mybooks = (By.XPATH, "/html/body/header[1]/div[3]/details/div[2]/ul/li[2]/a")
        self.profile = (By.XPATH,"/html/body/header[1]/div[3]/details/div[2]/ul/li[3]/a")
        self.settings = (By.XPATH, "/html/body/header[1]/div[3]/details/div[2]/ul/li[4]/a")
        self.logout = (By.XPATH, "/html/body/header[1]/div[3]/details/div[2]/ul/li[5]/form/button")
        #browse section
        self.subjects = (By.XPATH, "/html/body/header[1]/div[3]/details/div[2]/ul/li[7]/a")
        self.trending = (By.XPATH, "/html/body/header[1]/div[3]/details/div[2]/ul/li[8]/a")
        self.libexplorer = (By.XPATH, "/html/body/header[1]/div[3]/details/div[2]/ul/li[9]/a")
        self.lists = (By.XPATH, "/html/body/header[1]/div[3]/details/div[2]/ul/li[10]/a")
        self.collections = (By.XPATH, "/html/body/header[1]/div[3]/details/div[2]/ul/li[11]/a")
        self.k12 = (By.XPATH, "/html/body/header[1]/div[3]/details/div[2]/ul/li[12]/a")
        self.booktalks = (By.XPATH, "/html/body/header[1]/div[3]/details/div[2]/ul/li[13]/a")
        self.randombook = (By.XPATH, "/html/body/header[1]/div[3]/details/div[2]/ul/li[14]/a")
        self.advancedsearch = (By.XPATH, "/html/body/header[1]/div[3]/details/div[2]/ul/li[15]/a")
        #contribute section
        self.addbook = (By.XPATH, "/html/body/header[1]/div[3]/details/div[2]/ul/li[17]/a")
        self.recentedits = (By.XPATH, "/html/body/header[1]/div[3]/details/div[2]/ul/li[18]/a")
        #resources section
        self.helpsupport = (By.XPATH, "/html/body/header[1]/div[3]/details/div[2]/ul/li[20]/a")
        self.devcenter = (By.XPATH, "/html/body/header[1]/div[3]/details/div[2]/ul/li[21]/a")
        self.librarian_portal = (By.XPATH, "/html/body/header[1]/div[3]/details/div[2]/ul/li[22]/a")
    
    #functions    
    def side_mybooks(self):
        self.driver.find_element(*self.sidebar_button).click()
        time.sleep(1)
        self.driver.find_element(*self.mybooks).click()  
            
    def side_profile(self):
        self.driver.find_element(*self.sidebar_button).click()
        time.sleep(1)
        self.driver.find_element(*self.profile).click()
                
    def side_settings(self):
        self.driver.find_element(*self.sidebar_button).click()
        time.sleep(1)
        self.driver.find_element(*self.settings).click()
                
    def side_logout(self):
        self.driver.find_element(*self.sidebar_button).click()
        time.sleep(1)
        self.driver.find_element(*self.logout).click()
                
    def side_subjects(self):
        self.driver.find_element(*self.sidebar_button).click()
        time.sleep(1)
        self.driver.find_element(*self.subjects).click()
                
    def side_trending(self):
        self.driver.find_element(*self.sidebar_button).click()
        time.sleep(1)
        self.driver.find_element(*self.trending).click()
                
    def side_libexplorer(self):
        self.driver.find_element(*self.sidebar_button).click()
        time.sleep(1)
        self.driver.find_element(*self.libexplorer).click()
                
    def side_lists(self):
        self.driver.find_element(*self.sidebar_button).click()
        time.sleep(1)
        self.driver.find_element(*self.lists).click()
                
    def side_collections(self):
        self.driver.find_element(*self.sidebar_button).click()
        time.sleep(1)
        self.driver.find_element(*self.collections).click()
                
    def side_k12(self):
        self.driver.find_element(*self.sidebar_button).click()
        time.sleep(1)
        self.driver.find_element(*self.k12).click()
                
    def side_booktalks(self):
        self.driver.find_element(*self.sidebar_button).click()
        time.sleep(1)
        self.driver.find_element(*self.booktalks).click()
                
    def side_randombook(self):
        self.driver.find_element(*self.sidebar_button).click()
        time.sleep(1)
        self.driver.find_element(*self.randombook).click()
                
    def side_advancedsearch(self):
        self.driver.find_element(*self.sidebar_button).click()
        time.sleep(1)
        self.driver.find_element(*self.advancedsearch).click()
        
    def side_addbook(self):
        self.driver.find_element(*self.sidebar_button).click()
        time.sleep(1)
        self.driver.find_element(*self.addbook).click()
        
    def side_community_edits(self):
        self.driver.find_element(*self.sidebar_button).click()
        time.sleep(1)
        self.driver.find_element(*self.recentedits).click()
        
    def side_helpsupport(self):
        self.driver.find_element(*self.sidebar_button).click()
        time.sleep(1)
        self.driver.find_element(*self.helpsupport).click()
        
    def side_devcenter(self):
        self.driver.find_element(*self.sidebar_button).click()
        time.sleep(1)
        self.driver.find_element(*self.devcenter).click()
        
    def side_libportal(self):
        self.driver.find_element(*self.sidebar_button).click()
        time.sleep(1)
        self.driver.find_element(*self.librarian_portal).click()
    
