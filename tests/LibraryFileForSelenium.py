from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from time import sleep

class LibraryFileForSelenium():
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://www.flipkart.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)

    def getByType(self,locator):
        locator=locator.lower()
        if locator=="id":
            return By.ID
        elif locator=="xpath":
            return By.XPATH
        elif locator=="name":
            return By.NAME
        elif locator=="class_name":
            return By.CLASS_NAME

        return None

    def ElementWait(self,locator,locatorValue):
        byType=self.getByType(locator)
        i=1
        while(i<=20):
            try:
                self.driver.find_element(byType,locatorValue)
            except:
                sleep(1)
                i+=1

    def getScreenshot(self):
        path = "C:\\Users\\Ashwini\\PycharmProjects\\RobotFramewrok\\screenshots\\"
        name = str(round(time.time())) + ".png"
        value = path + name
        self.driver.save_screenshot(value)

    def validateTitle(self):
        expectedTitle = "Online Shopping Site for Mobiles, Electronics, Furniture, Grocery, Lifestyle, Books & More. Best Offers!"
        title = self.driver.title
        if expectedTitle != title:
            self.getScreenshot()
            assert expectedTitle == title

    def getLoginFields(self,locator,locatorValue):
        byType=self.getByType(locator)
        field=self.driver.find_element(byType,locatorValue)
        return field

    def login(self,usernameData,passwordData):
        username=self.getLoginFields("xpath","//input[@class='_2zrpKA _1dBPDZ']")
        username.send_keys(usernameData)
        password=self.getLoginFields("xpath","//input[@class='_2zrpKA _3v41xv _1dBPDZ']")
        password.send_keys(passwordData)
        loginButton=self.getLoginFields("xpath","//button[@class='_2AkmmA _1LctnI _7UHT_c']")
        loginButton.click()

    def getLoginUsername(self):
        sleep(10)
        name=self.getLoginFields("xpath","(//div[@class='_2aUbKa'])[1]")
        return name.text

# sel=LibraryFileForSelenium()
# sel.login("9742129882","Ashu@1704")