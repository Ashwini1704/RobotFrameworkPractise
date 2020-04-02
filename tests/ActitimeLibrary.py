from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
'''
Library file to launch the Actitime application in chrome browser and also some methods to perform action on the same application
'''
class ActitimeLibrary():
    '''
    Method Name : init
    Description : Method which is constructor to launch chrome browser, navigate to Actitime application whenever ActitimeLibrary class object is created.
    Arguments : self-object address
    Return : Nothing
    '''
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.get("https://online.actitime.com/capgemini1/login.do")
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)

    '''
    Method Name : createActionObject
    Description : Method to create ActionChains class 
    Arguments : self-object address
    Return : action
    '''
    def createActionObject(self):
        action=ActionChains(self.driver)
        return action

    '''
    Method Name : getByType
    Description : Method to return BY Types for id, xpath,name,class_name
    Arguments : self-object address, locator-id/xpath/name/class_name 
    Return : Return BY Types of locators as mentioned above, if other locators are passed then None is returned
    '''
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
        elif locator=="partial_link_text":
            return By.PARTIAL_LINK_TEXT
        return None

    '''
    Method Name : getScreenshot
    Description : Method to take screenshot of web page from application
    Arguments : self-object address
    Return : Nothing
    '''
    def getScreenshot(self):
        path = "C:\\Users\\Ashwini\\PycharmProjects\\RobotFramewrok\\screenshots\\"
        name = str(round(time.time())) + ".png"
        value = path + name
        self.driver.save_screenshot(value)

    '''
    Method Name : validateTitle
    Description : Method to validate the title of application home page
    Arguments : self-object address
    Return : Nothing
    '''
    def validateTitle(self):
        expectedTitle = "actiTIME - Login"
        title = self.driver.title
        if expectedTitle != title:
            self.getScreenshot()
            assert expectedTitle == title

    '''
    Method Name : getFields
    Description : Method to locate the elements in application
    Arguments : self-object address, locator-locator types, locatorValue-Value/path of locator
    Return : field - element of locator and locatorvalue in application
    '''
    def getFields(self,locator,locatorValue):
        byType=self.getByType(locator)
        field=self.driver.find_element(byType,locatorValue)
        return field
    '''
    Method Name : login
    Description : Method to login into the actitime application
    Arguments : self-object address, usernameData-username data, passwordData-password data
    Return : Nothing
    '''
    def login(self,usernameData,passwordData):
        username=self.getFields("id","username")
        username.send_keys(usernameData)
        password=self.getFields("name","pwd")
        password.send_keys(passwordData)
        loginButton=self.getFields("id","loginButton")
        loginButton.click()

    '''
    Method Name : clickNew
    Description : Method to click on New element in user page of actitime application
    Arguments : self-object address
    Return : Nothing
    '''
    def clickNew(self):
        # action=self.createActionObject()
        # wait=WebDriverWait(self.driver,20)
        # new=wait.until(EC.element_to_be_clickable((By.XPATH("//span[text()='New']"))))
        # new.click()
        new=self.getFields("xpath","//div[@id='addTaskButtonId']//div//span[contains(text(),'New')]")
        new.click()
        # action.double_click(new).perform()

    '''
    Method Name : selectProject
    Description : Method to select company name and project name in user tasks page
    Arguments : self-object address
    Return : Nothing
    '''
    def selectProject(self):
        companyField=self.getFields("xpath","(//div[@class='searchFilterPlaceholder '])[5]")
        companyField.click()
        sleep(2)
        companyName=self.getFields("xpath","//div[text()='- ALL ACTIVE CUSTOMERS -']")
        companyName.click()
        sleep(2)
        projectNameField=self.getFields("xpath","(//div[@class='searchFilterPlaceholder '])[6]")
        projectNameField.click()
        sleep(2)
        projectName=self.getFields("xpath","//div[text()='- ALL ACTIVE PROJECTS -']")
        projectName.click()

    '''
    Method Name : getNumberOfRows
    Description : Method to find the number of rows in dynamic table in task page
    Arguments : self-object address
    Return : len(numberOfRows)- integer which is the number of rows from numberOfRows list object
    '''
    def getNumberOfRows(self):
        numberOfRows = self.driver.find_elements_by_xpath("//table[@class='createTasksTable hideAddToTT']/tbody/tr")
        print(numberOfRows)
        print(len(numberOfRows))
        return len(numberOfRows)
    '''
    Method Name : dynamicTableHandle
    Description : Method to handle dynamic table in user task page
    Arguments : self-object address
    Return : Nothings
    '''
    def dynamicTableHandle(self):
        numberOfRows=self.getNumberOfRows()
        rows = "//table[@class='createTasksTable hideAddToTT']/tbody/tr"
        for i in range(1,numberOfRows+1):
            firstCol=self.driver.find_element_by_xpath(rows+"["+str(i)+"]//input[@class='inputFieldWithPlaceholder'][@placeholder='Enter task name']")
            secondCol=self.driver.find_element_by_xpath(rows+"["+str(i)+"]//input[@class='inputFieldWithPlaceholder'][@placeholder='not needed']")
            thirdCol=self.driver.find_element_by_xpath(rows+"["+str(i)+"]//button[text()='set deadline']")
            fourthCol=self.driver.find_element_by_xpath(rows+"["+str(i)+"]//div[@class='value ellipsis']")
            if i==1:
                firstCol.send_keys("Reading")
                secondCol.send_keys("2")
                thirdCol.click()
                setDate = self.driver.find_element_by_xpath("//span[text()='31']")
                setDate.click()
            elif i==2:
                firstCol.send_keys("Documentation")
                secondCol.send_keys("2")
                # thirdCol.click()
                # setDate = self.driver.find_element_by_xpath("//span[text()='31']")
                # setDate.click()
            elif i==3:
                firstCol.send_keys("Implementation")
                secondCol.send_keys("3")
                # thirdCol.click()
                # setDate = self.driver.find_element_by_xpath("//span[text()='31']")
                # setDate.click()
            else:
                pass

        createTaskButton=self.getFields("xpath","//div[text()='Create Tasks']")
        createTaskButton.click()

sel=ActitimeLibrary()
sel.login("nandeesha.kiccha0@gmail.com","Logistics@123")
sleep(20)
sel.clickNew()
sleep(10)
sel.getNumberOfRows()