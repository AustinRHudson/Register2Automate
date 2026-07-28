import time
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import json

#No input version in case you want to run this script through some type of scheduler like Windows scheduler, Cron, etc.
#Instead of the for loop that waits 23 hours inbetween each loop.

#Change values to the ones needed for your stay in the Values.json file.

with open('Values.json', 'r') as file:
    data = json.load(file)

messages = [data["apartmentNumber"], data["vehicleMake"], data["vehicleModel"], data["licensePlate"], data["licensePlate"]]

def waitForButton(driver, xPath):
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, xPath))
    )
    WebDriverWait(driver, 20).until(
        EC.invisibility_of_element((By.ID, "please-wait"))
    )

driver = webdriver.Firefox()
driver.get("https://www.register2park.com/register")
xPath = "//*[@id=\"propertyName\"]"
waitForButton(driver, xPath)
element = driver.find_element(By.XPATH, xPath)
element.send_keys(data["apartmentName"])
xPath = "//*[@id=\"confirmProperty\"]"
waitForButton(driver, xPath)
element = driver.find_element(By.XPATH, xPath)
element.click()
xPath = "/html/body/div[1]/div/div[2]/div[2]/div/form/div/div/button"
waitForButton(driver, xPath)
element = driver.find_element(By.XPATH, xPath)
element.click()

try:
    WebDriverWait(driver, 2).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div[6]/div/div/div[3]/button"))
    )
    element = driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div[3]/button")
    element.click()
    print("Button found and clicked!")
    WebDriverWait(driver, 20).until(
        EC.invisibility_of_element((By.XPATH, "/html/body/div[6]/div/div/div[3]/button"))
    )
except TimeoutException:
    print("Button not found. Safely moving on...")

xPath = "//*[@id=\"registrationTypeVisitor\"]"
waitForButton(driver, xPath)
element = driver.find_element(By.XPATH, xPath)
element.click()
apartmentNumberXPath = "//*[@id=\"vehicleApt\"]"
makeXPath = "//*[@id=\"vehicleMake\"]"
modelXPath = "//*[@id=\"vehicleModel\"]"
licensePlateXPath = "//*[@id=\"vehicleLicensePlate\"]"
confirmLicensePlateXPath = "//*[@id=\"vehicleLicensePlateConfirm\"]"
nextXPath = "//*[@id=\"vehicleInformation\"]"
paths = [apartmentNumberXPath, makeXPath, modelXPath, licensePlateXPath, confirmLicensePlateXPath]

waitForButton(driver, nextXPath)

for i in range(5):
    element = driver.find_element(By.XPATH, paths[i])
    element.send_keys(messages[i])

element = driver.find_element(By.XPATH, nextXPath)
element.click()
time.sleep(5)

driver.close()