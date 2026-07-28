import time
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import json

from Register2Automate.RegisterAutomation import registerAutomate

#No input version in case you want to run this script through some type of scheduler like Windows scheduler, Cron, etc.
#Instead of the for loop that waits 23 hours inbetween each loop.

#Change values to the ones needed for your stay in the Values.json file.

with open('Values.json', 'r') as file:
    data = json.load(file)

messages = [data["apartmentNumber"], data["vehicleMake"], data["vehicleModel"], data["licensePlate"], data["licensePlate"]]

driver = webdriver.Firefox()

registerAutomate(driver, data["apartmentName"], messages, data["accessCode"])

nextXPath = "//*[@id=\"vehicleInformation\"]"
element = driver.find_element(By.XPATH, nextXPath)
element.click()
time.sleep(5)

driver.close()