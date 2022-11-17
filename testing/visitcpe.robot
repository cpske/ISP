*** Settings ***
Documentation     View the CPE Homework using a Web Browser
Library           SeleniumLibrary

*** Variables ***
${SITE_URL}    https://www.cpe.ku.ac.th
${BROWSER}     Firefox

*** Test Cases ***
Test the CPE Homework
    Visit CPE Homepage
    Title Should Be      Department of Computer Engineering - Faculty of Engineering Kasetsart University
    Location Should Be   ${SITE_URL}
    Page Should Contain  ABOUT

*** Keywords ***
# user defined expressions and actions

Visit CPE Homepage
    Open Browser  ${SITE_URL}  ${BROWSER}
