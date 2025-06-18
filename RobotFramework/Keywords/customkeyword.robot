*** Settings ***
Resource    ../utility/Helpers.robot

*** Keywords ***
open & close Browser
    open Browser    ${flip_url}      ${browser}
    Maximize Browser Window
    Wait for and click on element   ${button}   5
#    CLICK ELEMENT    ${button}
    Wait for and click on element   ${clk_on_mob}   5
#    CLICK ELEMENT    ${clk_on_mob}
    Scroll Element Into View    ${brand_name}
    Wait for and click on element   ${brand_name}   5
#    CLICK ELEMENT    ${brand_name}
    ${title} =  Get Window Titles
    #we can also use log(which will print in report)
    #log    ${title}
    log to console     ${title}
    Switch Window       ${title}[1]
    ${all_title} =  Get Title
    log to console    ${all_title}

open browser & shop
    open Browser    ${flip_url}      ${browser}
    Maximize Browser Window
    Wait for and click on element   ${button}   5
    mouse over    ${lnk_fassion}
    Wait for and click on element    ${clk_mens_wear}   5
    Scroll to element and click    ${ele_shirt}
    wait for element    5
    ${titles} =  Get Window Titles
    Switch Window       ${titles}[1]
    wait for element    5
##    Scroll to element and click     ${lnk_size}
#    ${size_txt} =   GET TEXT    ${lnk_size}
#    log to console    ${size_txt}
    Scroll to element and click    ${size_select}
    wait for element    5
    ${get_text} =
