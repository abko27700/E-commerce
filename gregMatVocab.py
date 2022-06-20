from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

def gregMatHelper():
    options = webdriver.ChromeOptions()
    options.add_argument("user-data-dir=C:\\Windows.old\\Users\\Abhishek\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH,chrome_options=options)
    driver.get("https://quizlet.com/in/501823268/set-1-flash-cards/")
    buttonFinder="//svg[@aria-label='arrow right']"
    nextButton = driver.find_element(by=By.XPATH,value=buttonFinder)
    nextButton.click()
    count=1

    while count <=29:
        
        count+=1
    

gregMatHelper()