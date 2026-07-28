import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#No input version in case you want to run this script through some type of scheduler like Windows scheduler, Cron, etc.
#Instead of the for loop that waits 23 hours inbetween each loop.

#Change values to the ones needed for your stay.
apartmentName = ""

apartmentNumber = ""
vehicleMake = ""
vehicleModel = ""
vehicleLicensePlate = ""
messages = [apartmentNumber, vehicleMake, vehicleModel, vehicleLicensePlate ,vehicleLicensePlate]

driver = webdriver.Firefox()
driver.get("https://www.register2park.com/register")
xPath = "//*[@id=\"propertyName\"]"
time.sleep(2)
element = driver.find_element(By.XPATH, xPath)
element.send_keys(apartmentName)
xPath = "//*[@id=\"confirmProperty\"]"
element = driver.find_element(By.XPATH, xPath)
element.click()
time.sleep(2)
xPath = "/html/body/div[1]/div/div[2]/div[2]/div/form/div/div/button"
element = driver.find_element(By.XPATH, xPath)
element.click()
time.sleep(2)
xPath = "//*[@id=\"registrationTypeVisitor\"]"
element = driver.find_element(By.XPATH, xPath)
element.click()
time.sleep(2)
apartmentNumberXPath = "//*[@id=\"vehicleApt\"]"
makeXPath = "//*[@id=\"vehicleMake\"]"
modelXPath = "//*[@id=\"vehicleModel\"]"
licensePlateXPath = "//*[@id=\"vehicleLicensePlate\"]"
confirmLicensePlateXPath = "//*[@id=\"vehicleLicensePlateConfirm\"]"
nextXPath = "//*[@id=\"vehicleInformation\"]"
paths = [apartmentNumberXPath, makeXPath, modelXPath, licensePlateXPath, confirmLicensePlateXPath]

for i in range(5):
    element = driver.find_element(By.XPATH, paths[i])
    element.send_keys(messages[i])

element = driver.find_element(By.XPATH, nextXPath)
#element.click()
time.sleep(3)
driver.close()