*** Settings ***
Library  SeleniumLibrary


*** Variables ***
${url}      https://www.flipkart.com/
${browser}  chrome

*** Test Cases ***
Login_Test
#    open Browser    https://www.flipkart.com/   chrome
     open Browser   ${url}      ${browser}



*** Keywords ***

