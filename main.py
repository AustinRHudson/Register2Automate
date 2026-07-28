import time
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

from Register2Automate.RegisterAutomation import registerAutomate

oneDay = 86400

apartmentName = input("What is the name of the apartment you will be staying at? \n")

accessCode = input("If there is an access code, what is the code? (Skip this if there is no code)")

messages = []
message = input("What is the apartment number of where you are going to be staying? \n")
messages.append(message)
message = input("What make is your vehicle? \n")
messages.append(message)
message = input("What model is your vehicle? \n")
messages.append(message)
message = input("What is the license plate number of your vehicle? \n")
messages.append(message)
messages.append(message)

dayAmounnt = int(input("How many days will you be staying? \n"))
driver = webdriver.Firefox()
for i in range(dayAmounnt):
    driver.get("https://www.register2park.com/register")

    registerAutomate(driver, apartmentName, messages, accessCode)

    nextXPath = "//*[@id=\"vehicleInformation\"]"
    element = driver.find_element(By.XPATH, nextXPath)
    element.click()
    time.sleep(oneDay)

driver.close()