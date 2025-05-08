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
    #my open library category
    def side_mybooks(self):   #clicking on my books on the sidebar
        self.driver.find_element(*self.sidebar_button).click()
        time.sleep(1)
        self.driver.find_element(*self.mybooks).click()  
            
    def side_profile(self):   #clicking on my profile on the sidebar
        self.driver.find_element(*self.sidebar_button).click()
        time.sleep(1)
        self.driver.find_element(*self.profile).click()
                
    def side_settings(self):  #clicking on settings on the sidebar
        self.driver.find_element(*self.sidebar_button).click()
        time.sleep(1)
        self.driver.find_element(*self.settings).click()
                
    def side_logout(self):   #clicking on logout button on the sidebar
        self.driver.find_element(*self.sidebar_button).click()
        time.sleep(1)
        self.driver.find_element(*self.logout).click()

    #browse category
    def side_subjects(self):   #clicking on subjects on the sidebar
        self.driver.find_element(*self.sidebar_button).click()
        time.sleep(1)
        self.driver.find_element(*self.subjects).click()
                
    def side_trending(self):   #clicking on trending on the sidebar
        self.driver.find_element(*self.sidebar_button).click()
        time.sleep(1)
        self.driver.find_element(*self.trending).click()
                
    def side_libexplorer(self): #clicking on library explorer on the sidebar
        self.driver.find_element(*self.sidebar_button).click()
        time.sleep(1)
        self.driver.find_element(*self.libexplorer).click()
                
    def side_lists(self):   #clicking on lists on the sidebar
        self.driver.find_element(*self.sidebar_button).click()
        time.sleep(1)
        self.driver.find_element(*self.lists).click()
                
    def side_collections(self):   #clicking on collections on the sidebar
        self.driver.find_element(*self.sidebar_button).click()
        time.sleep(1)
        self.driver.find_element(*self.collections).click()
                
    def side_k12(self):   #clicking on k-12 student library on the sidebar
        self.driver.find_element(*self.sidebar_button).click()
        time.sleep(1)
        self.driver.find_element(*self.k12).click()
                
    def side_booktalks(self):   #clicking on book talks on the sidebar
        self.driver.find_element(*self.sidebar_button).click()
        time.sleep(1)
        self.driver.find_element(*self.booktalks).click()
                
    def side_randombook(self):   #clicking on random book on the sidebar
        self.driver.find_element(*self.sidebar_button).click()
        time.sleep(1)
        self.driver.find_element(*self.randombook).click()
                
    def side_advancedsearch(self):   #clicking on advanced search on the sidebar
        self.driver.find_element(*self.sidebar_button).click()
        time.sleep(1)
        self.driver.find_element(*self.advancedsearch).click()
    
    #contribute category
    def side_addbook(self):   #clicking on add book on the sidebar
        self.driver.find_element(*self.sidebar_button).click()
        time.sleep(1)
        self.driver.find_element(*self.addbook).click()
        
    def side_community_edits(self):   #clicking on recent community edits on the sidebar
        self.driver.find_element(*self.sidebar_button).click()
        time.sleep(1)
        self.driver.find_element(*self.recentedits).click()
    
    #resources category
    def side_helpsupport(self):   #clicking on help & support on the sidebar
        self.driver.find_element(*self.sidebar_button).click()
        time.sleep(1)
        self.driver.find_element(*self.helpsupport).click()
        
    def side_devcenter(self):   #clicking on development center on the sidebar
        self.driver.find_element(*self.sidebar_button).click()
        time.sleep(1)
        self.driver.find_element(*self.devcenter).click()
        
    def side_libportal(self):   #clicking on library portal on the sidebar
        self.driver.find_element(*self.sidebar_button).click()
        time.sleep(1)
        self.driver.find_element(*self.librarian_portal).click()
    
