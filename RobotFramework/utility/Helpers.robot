*** Settings ***
Library     SeleniumLibrary
Resource  ../Keywords/customkeyword.robot
Resource    ../Variables/newvariables.robot

*** Keywords ***
Wait for and click on element
    [Arguments]     ${element1}     ${time}
    Wait Until Element Is Visible       ${element1}     ${time}
    click element    ${element1}

Scroll to element and click
    [Arguments]    ${element3}
    scroll element into view        ${element3}
    click element     ${element3}

wait for element
    [Arguments]    ${time1}
    sleep    ${time1}