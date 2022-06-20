from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time


def bmsTest():
    options = webdriver.ChromeOptions()
    options.add_argument("user-data-dir=C:\\Windows.old\\Users\\Abhishek\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH,chrome_options=options)
    driver.get("https://in.bookmyshow.com/explore/home/national-capital-region-ncr")       
    moviePath="//div[@data-content='Bhool Bhulaiyaa 2']"
    movieFinder = WebDriverWait(driver,50).until(lambda driver: driver.find_element(by=By.XPATH,value=moviePath))
    movieFinder.click()
    bookTicketsPath="//span[text()='Book tickets']"
    bookTicketsFinder=WebDriverWait(driver,50).until(lambda driver: driver.find_element(by=By.XPATH,value=bookTicketsPath))
    bookTicketsFinder.click()
    venueListPath="//li[@class='list']"
    venueListFinder=WebDriverWait(driver,50).until(lambda driver: driver.find_elements(by=By.XPATH,value=venueListPath))
    for venue in venueListFinder:
        print (venue.get_attribute('data-name'))
    time.sleep(60)

bmsTest()