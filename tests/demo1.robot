*** Settings ***
Library  SeleniumLibrary
Library    ./LibraryFileForSelenium.py
#Library    C:/Users/Ashwini/PycharmProjects/RobotFramewrok/LibrariesForSelenium/LibrarySelenium.py
Test Setup  Launch Browser  ${URL}  ${Browser}
Test Teardown  Close Browser

*** Variables ***
${URL}  https://www.facebook.com/login.php
${Browser}  chrome
${username}  9742129882
${password}  Ashu@1704
@{USN_PWD}  9742129882  Ashu@1704
${rows}  //div[3]/div[1]/div[1]/table/tbody/tr

*** Keywords ***
Console something
    [Documentation]  DEPRECATED
    Log  Console something

Launch Browser
    [Arguments]  ${URLToLaunch}  ${browser}=chrome
    open browser  ${URLToLaunch}  ${browser}

Close Browser
    close all browsers

Input Username
    [Arguments]  ${usn}
    input text  email  ${usn}

Input Password
    [Arguments]  ${pwd}
    input text  pass  ${pwd}

Input Fields
    [Arguments]    @{USN_PWD}
    input text  id=email  @{USN_PWD}[0]
    input text  id=pass  @{USN_PWD}[1]

Click LoginButton
    click button  loginbutton

Testing Varargs
    [Arguments]  ${required}  ${optional}=HI  @{items}
    Log  1ST Argument is ${required}
    log  2ND argumnet is default ${optional}
    :FOR  ${other}  IN RANGE  @{items}
    \   LOG  ${other}
*** Test Cases ***
#LoginFacebook
#    Launch Browser  ${URL}
#    log  Browser launched
#    sleep  5s
#    Input Username  ${username}
#    sleep  2s
#    Input Password  ${password}
#    sleep  3s
##    Input Fields  @{USN_PWD}
#    Click LoginButton

#VarArgs
#    Testing Varargs  Hello  I  AM  Ashwini  T  M

Concate
#    ${concate}=  catenate  SEPARATOR=  ${rows}  [  1  ]//td[1]/input
#    LOG  ${concate}
    ${row}=   ${rows}
    ${row}=  convert to number  ${row}
    log  ${row}