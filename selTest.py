from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

def whatsapp_message(contact,message):

    options = webdriver.ChromeOptions()
    options.add_argument("user-data-dir=C:\\Windows.old\\Users\\Abhishek\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH,chrome_options=options)
    driver.get("https://web.whatsapp.com/")


    inp_xpath_search = "//div[@title='Search input textbox']"
    input_box_search = WebDriverWait(driver,50).until(lambda driver: driver.find_element(by=By.XPATH,value=inp_xpath_search))
    #input_box_search=driver.find_element(by=By.XPATH,value=inp_xpath_search)
    input_box_search.click()
    time.sleep(2)
    input_box_search.send_keys(contact)
    time.sleep(2)

    inp_xpath_contact="//span[@title='"+contact+"']"
    selected_contact = driver.find_element(by=By.XPATH,value=inp_xpath_contact)
    selected_contact.click()

    inp_xpath = '//div[@title="Type a message"]'
    input_box = driver.find_element(by=By.XPATH,value=inp_xpath)
    time.sleep(2)
    #input_box.send_keys(message + Keys.ENTER)
    time.sleep(2)

   # driver.quit()

    #search=driver.find_element(by=By.XPATH,value="[title*='Search input textbox']")
    #search.send_keys("Daddy")
    #search.send_keys(Keys.ENTER) 


contact1 = "Daddy"
contact2 = "Birthgiver"
message = "Amarnath Helicopter Booking Has Started!"
whatsapp_message(contact1,message)