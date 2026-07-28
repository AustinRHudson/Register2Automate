import time
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

def waitForButton(driver, xPath):
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, xPath))
    )
    WebDriverWait(driver, 20).until(
        EC.invisibility_of_element((By.ID, "please-wait"))
    )

def findElementAndClick(driver, xPath):
    waitForButton(driver, xPath)
    element = driver.find_element(By.XPATH, xPath)
    element.click()

oneDay = 86400

apartmentName = input("What is the name of the apartment you will be staying at? \n")

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

    xPath = "//*[@id=\"propertyName\"]"
    waitForButton(driver, xPath)
    element = driver.find_element(By.XPATH, xPath)
    element.send_keys(apartmentName)

    xPath = "//*[@id=\"confirmProperty\"]"
    findElementAndClick(driver, xPath)

    xPath = "/html/body/div[1]/div/div[2]/div[2]/div/form/div/div/button"
    findElementAndClick(driver, xPath)

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
    findElementAndClick(driver, xPath)

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
    time.sleep(oneDay)

driver.close()