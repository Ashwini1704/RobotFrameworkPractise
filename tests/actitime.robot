'''

'''
*** Settings ***
Library  SeleniumLibrary
Library  ./ActitimeLibrary.py

*** Variables ***
${rows}  //table[@class='createTasksTable hideAddToTT']/tbody/tr
${username}  nandeesha.kiccha0@gmail.com
${password}  Logistics@123

*** Keywords ***
DynamicTable
    ${numberOfRows}=  getNumberOfRows
    ${numberOfRows}=  convert to number  ${numberOfRows}
    :For  ${index}  IN RANGE  1  ${numberOfRows}+1
    \  ${firstCol}=  catenate  SEPARATOR=  ${rows}  [  ${index}  ]//input[@class='inputFieldWithPlaceholder'][@placeholder='Enter task name']
    \  input text  xpath=${firstCol}  Documentation
    \  ${secondCol}=  catenate  SEPARATOR=  ${rows}  [  ${index}  ]//input[@class='inputFieldWithPlaceholder'][@placeholder='not needed']
    \  input text  xpath=${secondCol}  2
    \  ${thirdCol}=  catenate  SEPARATOR=  ${rows}  [  ${index}  ]//button[text()='set deadline']
    \  click element  xpath=${thirdCol}
    \  ${setDate}=  click element  xpath=//span[text()='31']
    \  ${forthCol}=  catenate  SEPARATOR=  ${rows}  [  ${index}  ]//div[@class='value ellipsis']
    \  click element  xpath=${forthCol}
    \  exit for loop if  ${index}>=2
    click element  xpath=//div[text()='Create Tasks']

*** Test Cases ***
HandleDynamicTableUsingForInRange
    run keyword  login  ${username}  ${password}
    sleep  30s
    run keyword  clickNew
    sleep  2s
    run keyword  selectProject
    sleep  2s
    run keyword  DynamicTable
    sleep  2s
#    close browser


