#import selenium and pytest related libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pytest 
import time

#import pages containing XPATH and function definitions
from pages.homepage import homePage
from pages.login_page import loginPage
from pages.signup_page import signupPage
from pages.searchpage import searchPage
from pages.readbook import readBook
from pages.sidebar import sidebarPage

@pytest.fixture(scope="module")
def driver(): #initialization for browser
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
    
def test_open_homepage(driver): #opening the openlibrary homepage
    home_page = homePage(driver)
    home_page.openpage("https://openlibrary.org/")
    driver.maximize_window()
    time.sleep(2)
    
def test_signup(driver):  #checking if signup link and page works
    signup_page = signupPage(driver)
    signup_page.signup()
    signup_page.email("newabiki24@gmail.com")
    time.sleep(1)
    signup_page.username("btesting")
    time.sleep(1)
    signup_page.password("2024@zeta")
    time.sleep(3)
    #signup_page.click_signup()  #disabling the signup button to prevent attempting to sign up duplicate test accounts
    
def test_switching_signup_login(driver):  #test switching between login and signup pages via hyperlink
    signup_page = signupPage(driver)
    signup_page.click_login_link()
    time.sleep(2)
    signup_page.click_signup_link()
    time.sleep(2)

#parameetrizing username and password to be inputed in quick succession
@pytest.mark.parametrize("email, password", [("newabiki24gmail", "2024@zeta"),        #invalid email without @
                                             ("newabiki24@gm", "2024@zeta"),          #invalid email with @
                                             ("newabiki25@gmail.com", "2024@zet"),    #wrong email wrong password
                                             ("newabiki25@gmail.com", "2024@zeta"),   #wrong email correct password    
                                             ("newabiki24@gmail.com", "2024@zet")])   #correct email wrong password

def test_badlogin(driver, email, password):  #bad input parameters function for testing
    login_page = loginPage(driver)
    homePage(driver).login()
    login_page.email(email)
    time.sleep(1)
    login_page.password(password)
    time.sleep(1)
    login_page.click_login()
    time.sleep(3)
    
def test_login(driver):   #function with valid input parameters, seperated from previous function to skip bad logins if desired
    login_page = loginPage(driver)
    if(driver.title != "https://openlibrary.org/account/login"):
        {
                homePage(driver).login()
        }
    time.sleep(1)
    login_page.email("newabiki24@gmail.com")
    time.sleep(1)
    login_page.password("2024@zeta")
    time.sleep(1)
    login_page.click_login()
    time.sleep(3)

def test_navbar(driver):  #to test every elements present in the navigation bar at the top of the screen
    home_page = homePage(driver)
    home_page.open_mybooks()
    time.sleep(3)
    home_page.open_subjects()
    time.sleep(1)
    home_page.open_trending()
    time.sleep(1)
    home_page.open_libraryexplorer()
    time.sleep(1)
    home_page.open_lists()
    time.sleep(1)
    # home_page.open_collections()
    # time.sleep(1)
    home_page.open_k12()
    time.sleep(1)
    home_page.open_booktalks()
    time.sleep(4)
    home_page.openpage("https://openlibrary.org/")
    time.sleep(1)
    home_page.open_randombook()
    time.sleep(1)
    home_page.open_advancedsearch()
    time.sleep(3)
    
def test_barcode(driver):  #function to test functionality of the barcode search button
    search_page = searchPage(driver)
    search_page.click_barcode()
    time.sleep(5)
    driver.back()
    time.sleep(5)
    
def test_footer(driver):  #to scroll all the way down to the footer in order to inspect footer elements then returning to the top
    home_page = homePage(driver)
    page_height = driver.execute_script("return document.body.scrollHeight")
    scroll_speed = 800
    scroll_iteration = int(page_height/scroll_speed)
    
    for _ in range(scroll_iteration):   
        driver.execute_script(f"window.scrollBy(0,{scroll_speed});")
        time.sleep(3)
        
    time.sleep(2)
    home_page.returntotop()
    time.sleep(3)
    
def test_searchbook(driver):  #to search for War and Peace book and inspect book details
    search_page = searchPage(driver)
    search_page.searchbar("War and Peace")
    time.sleep(1)
    search_page.clickby_href("/works/OL267171W/War_and_Peace?edition=key%3A/books/OL10276911M")
    time.sleep(3)
    page_height = driver.execute_script("return document.body.scrollHeight")
    
    scroll_speed = 400
    scroll_iteration = int(page_height/scroll_speed)
    
    for _ in range(scroll_iteration):   
        driver.execute_script(f"window.scrollBy(0,{scroll_speed});")
        time.sleep(2)
        
    time.sleep(2)
    homePage(driver).returntotop()
    time.sleep(3)
    
def test_borrowbook(driver):  #borrow and read the book war and peace
    read_book = readBook(driver)
    read_book.click_borrow()
    time.sleep(6)
    
    for i in range(5):
        time.sleep(1)
        read_book.nextpage()
        time.sleep(2)
    
    driver.back()    
    time.sleep(3)

def test_resize_window(driver):  #resize window dynamically
    home_page = homePage(driver)
    driver.set_window_size(1024, 768)
    time.sleep(2)
    home_page.openlib()
    time.sleep(2)
    home_page.open_subjects()
    time.sleep(2)
    driver.maximize_window()
    time.sleep(3)
    
def test_advanced_search(driver):  #to test the functionality of advanced search features
    home_page = homePage(driver)
    search_page = searchPage(driver)
    home_page.open_advancedsearch()
    time.sleep(2)
    search_page.author("Scott Westerfeld")
    time.sleep(2)
    search_page.subject("War")
    time.sleep(2)
    search_page.ad_search()
    time.sleep(2)
    driver.execute_script("window.scrollBy(0, 600);")
    time.sleep(5)
    
def test_search_errorhandling(driver):  #to test how search handles invalid queries
    search_page = searchPage(driver)
    search_page.searchbar("zbc1234")
    time.sleep(1)
    search_page.clearbar()
    time.sleep(1)
    search_page.searchbar("")
    time.sleep(3)
    
def test_sidebar(driver):  #to run through all the button of the sidebar to test its functionality
    sidebar_page = sidebarPage(driver)
    sidebar_page.side_mybooks()
    time.sleep(1)
    sidebar_page.side_profile()
    time.sleep(1)
    sidebar_page.side_settings()
    time.sleep(1)
    sidebar_page.side_logout()
    time.sleep(1)
    test_login(driver)
    sidebar_page.side_subjects()
    time.sleep(1)
    sidebar_page.side_trending()
    time.sleep(1)
    sidebar_page.side_libexplorer()
    time.sleep(3)
    sidebar_page.side_lists()
    time.sleep(1)
    sidebar_page.side_collections()
    time.sleep(1)
    sidebar_page.side_k12()
    time.sleep(1)
    sidebar_page.side_booktalks()
    time.sleep(5)
    homePage(driver).openpage("https://openlibrary.org/")
    time.sleep(3)
    sidebar_page.side_randombook()
    time.sleep(1)
    sidebar_page.side_advancedsearch()
    time.sleep(1)
    sidebar_page.side_addbook()
    time.sleep(1)
    sidebar_page.side_community_edits()
    time.sleep(1)
    sidebar_page.side_helpsupport()
    time.sleep(1)
    sidebar_page.side_devcenter()
    time.sleep(1)
    sidebar_page.side_libportal()
    time.sleep(5) 
    
def test_loggingout_from_mybooks(driver):  #to log out from my books page
    home_page = homePage(driver)
    home_page.open_mybooks()
    time.sleep(1)
    sidebarPage(driver).side_logout()
    time.sleep(1)
    driver.execute_script("window.scrollBy(0, 400);")
    time.sleep(5)