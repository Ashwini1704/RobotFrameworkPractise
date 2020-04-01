from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from time import sleep

class LibrarySelenium():
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://www.flipkart.com/")
        self.driver.maximize_window()

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

    def implicitWait(self,locator,locatorValue):
        byType=self.getByType(locator)
        i=1
        while(i<=20):
            try:
                self.driver.find_element(byType,locatorValue)
                break
            except:
                sleep(1)
                i+=1

    def getScreenshot(self):
        path="C:\\Users\\Ashwini\\PycharmProjects\\RobotFramewrok\\screenshots\\"
        name=str(round(time.time()))+".png"
        value=path+name
        self.driver.save_screenshot(value)

    def validateTitle(self):
        expectedTitle="Online Shopping Site for Mobiles, Electronics, Furniture, Grocery, Lifestyle, Books & More. Best Offers!"
        title=self.driver.title
        if expectedTitle!=title:
            self.getScreenshot()
            assert expectedTitle==title


sel=LibrarySelenium()
sel.validateTitle()