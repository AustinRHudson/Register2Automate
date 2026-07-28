import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

apartmentName = input("What is the name of the apartment you will be staying at?")

messages = []
message = input("What is the apartment number of where you are going to be staying?")
messages.append(message)
message = input("What make is your vehicle?")
messages.append(message)
message = input("What model is your vehicle?")
messages.append(message)
message = input("What is the license plate number of your vehicle?")
messages.append(message)
messages.append(message)

dayAmounnt = int(input("How many days will you be staying?"))
driver = webdriver.Firefox()
for i in range(dayAmounnt):
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