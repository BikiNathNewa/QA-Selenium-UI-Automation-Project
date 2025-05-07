#contains XPATH and functions regarding homepage 
from selenium.webdriver.common.by import By
import time

class homePage:
    def __init__(self,driver):
        self.driver = driver
        self.navbar_mybooks = (By.XPATH, "/html/body/header[1]/ul[1]/li[1]/div/a") 
        self.navbar_browse = (By.XPATH, "//*[@id='header-bar']/ul[1]/li[2]/div/details/summary")
        self.navbar_openlib = (By.XPATH, "/html/body/header[1]/div[1]/a/div/img")
                
        #browse sub-section
        self.nb_subjects = (By.XPATH, "/html/body/header[1]/ul[1]/li[2]/div/details/div/ul/li[1]/a")
        self.nb_trending = (By.XPATH, "/html/body/header[1]/ul/li[2]/div/details/div/ul/li[2]/a")
        self.nb_libraryexplorer = (By.XPATH, "/html/body/header[1]/ul/li[2]/div/details/div/ul/li[3]/a")
        self.nb_lists = (By.XPATH, "/html/body/header[1]/ul/li[2]/div/details/div/ul/li[4]/a")
        self.nb_collections = (By.XPATH, "/html/body/header[1]/ul/li[2]/div/details/div/ul/li[5]/a")
        self.nb_k12 = (By.XPATH, "/html/body/header[1]/ul/li[2]/div/details/div/ul/li[6]/a")
        self.nb_booktalks = (By.XPATH, "/html/body/header[1]/ul/li[2]/div/details/div/ul/li[7]/a")
        self.nb_randombook = (By.XPATH, "/html/body/header[1]/ul/li[2]/div/details/div/ul/li[8]/a")
        self.nb_advancedsearch = (By.XPATH, "/html/body/header[1]/ul/li[2]/div/details/div/ul/li[9]/a")
        
        #signup and login
        self.navbar_signup = (By.XPATH, "/html/body/header[1]/ul[2]/li[2]/a")
        self.navbar_login = (By.XPATH,"/html/body/header[1]/ul[2]/li[1]/a")
        
        #footer
        self.footer_returntotop = (By.XPATH, "/html/body/footer/div/div[1]/div[2]/ul/li[7]/a")
    
    def openpage(self,url):
        self.driver.get(url)
        
    def open_mybooks(self):
        self.driver.find_element(*self.navbar_mybooks).click()  
             
    def open_subjects(self):
        self.driver.find_element(*self.navbar_browse).click()
        time.sleep(1)
        self.driver.find_element(*self.nb_subjects).click()  
 
    def open_trending(self):
        self.driver.find_element(*self.navbar_browse).click()
        time.sleep(1)
        self.driver.find_element(*self.nb_trending).click()  
        
    def open_libraryexplorer(self):
        self.driver.find_element(*self.navbar_browse).click()
        time.sleep(1)
        self.driver.find_element(*self.nb_libraryexplorer).click()  

    def open_lists(self):
        self.driver.find_element(*self.navbar_browse).click()
        time.sleep(1)
        self.driver.find_element(*self.nb_lists).click()  
        
    def open_collections(self):
        self.driver.find_element(*self.navbar_browse).click()
        time.sleep(1)
        self.driver.find_element(*self.nb_collections).click()  

    def open_k12(self):
        self.driver.find_element(*self.navbar_browse).click()
        time.sleep(1)
        self.driver.find_element(*self.nb_k12).click()  

    def open_booktalks(self):
        self.driver.find_element(*self.navbar_browse).click()
        time.sleep(1)
        self.driver.find_element(*self.nb_booktalks).click()     
        
    def open_randombook(self):
        self.driver.find_element(*self.navbar_browse).click()
        time.sleep(1)
        self.driver.find_element(*self.nb_randombook).click()  
        
    def open_advancedsearch(self):
        self.driver.find_element(*self.navbar_browse).click()
        time.sleep(1)
        self.driver.find_element(*self.nb_advancedsearch).click()      
    
    def login(self):
        self.driver.find_element(*self.navbar_login).click()
        
    def returntotop(self):
        self.driver.find_element(*self.footer_returntotop).click()

    def openlib(self):
        self.driver.find_element(*self.navbar_openlib).click()