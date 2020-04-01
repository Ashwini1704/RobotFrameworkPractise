*** Settings ***
Library  SeleniumLibrary
Library  ./LibraryFileForSelenium.py

*** Variables ***
${usernameData}  9900932956
${passwordData}  Logistics@123

*** Keywords ***
login
    [Arguments]  ${usernameData}  ${passwordData}
    ${username}=  getLoginFields  xpath  //input[@class='_2zrpKA _1dBPDZ']
    input text  ${username}    ${usernameData}
    ${password}=  getLoginFields  xpath  //input[@class='_2zrpKA _3v41xv _1dBPDZ']
    input text  ${password}  ${passwordData}
    ${loginButton}=  getLoginFields  xpath  //button[@class='_2AkmmA _1LctnI _7UHT_c']
    click button  ${loginButton}

*** Test Cases ***
Title Validation
    [Documentation]  Validating the correct url is opened or not by fetching the title and validating
    run keyword  validateTitle

Login Flipkart
    [Documentation]  Login into the flipkart application
    sleep  5s
    run keyword  login  ${usernameData}  ${passwordData}
    ${usernameLoggedIn}=  getLoginUsername
    Log  ${usernameLoggedIn}
