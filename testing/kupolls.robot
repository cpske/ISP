*** Settings ***
#                 This works with Jindaporn's KU Polls main branch code.
#                 If you want to uncomment the test "Title Should Be" (below)
#                 then, in polls/templates/polls/index.html add
#                 <title>KU Polls</title>

Documentation     Login and Submit a Vote in KU Polls
Library           SeleniumLibrary
Library           String
Library           Dialogs

# Suite settings can be used to start a browser window 
# before tests and do something after all tests,
# instead of creating a new browser window ('Open Browser') in each test.
#Suite Setup      Open Browser  Firefox
Suite Teardown    Close Browser

*** Variables ***
${SITE_URL}       http://localhost:8000/
${BROWSER}        Firefox
# I added a <title>KU Polls</title> to the index.html template.
${page title}     KU Polls
${page_header}    KU Polls
${username}       nobi
${password}       nobita00

*** Test Cases ***
# Tests are run in the order listed (unlike JUnit and unittest)

Visit Home Page and Select a Poll
    # Slow the script execution so we can see what's happening
    #Set Delay 1 Seconds
    Open Browser                ${SITE_URL}  ${BROWSER}
	Polls Page Should be Open
    Comment                     Page should contain something to vote on
    Page Should Contain Button  Vote
    Click Button                Vote

Can Login
    ${login_url} =              Catenate  ${SITE_URL}accounts/login/
    Log To Console              ${\n}We are redirected to ${login_url}${\n}
    # The actual URL has a query param, so use an inexact match
    Location Should Contain     ${login_url}
    Input Text                  name:username  ${username}
    Input Password              name:password  ${password}
    Click Button                Login
    Comment                     We are redirected to where?
    ${redirect_url} =           Get Location
    Log To Console              ${\n}After Login we are redirected to ${redirect_url}${\n}

Vote for a Poll
    Log To Console              ${\n}Anyone want to write this?${\n}

Shutdown
    # prompt user to close browser window
    Pause Execution             Click OK to close browser window


*** Keywords ***
# Keywords are tasks that you define. They can have parameters.
# You invoke Keywords from your "Test" or "Tasks".


Polls Page Should Be Open
    # be careful of URLs. Test will fail if it doesn't EXACTLY match.
    ${polls_index} =      Catenate  ${SITE_URL}polls/
    Location Should Be    ${polls_index}
    # This test requires the page contain a <title>...</title> (it should!)
    # Title Should Be       ${page title}
	Page Should Contain   ${page header}

Set Delay ${seconds} Seconds
    # This is a SeleniumLibrary keyword to 
    Set Selenium Speed    ${seconds} seconds

Should Greet User By Name
    Comment               After Login, the page should greet the user by name
    ${name} =             Convert To Title Case  ${username}
    Page Should Contain   Hello, ${name}

### Unused Examples ###
#Open Login Page
#    New Browser  ${BROWSER}
#    New Page     ${SITE_URL}
#    Login Page Should Be Open
#
#Input Credentials ${username} ${password}
#    Type Text    text=Username    ${username}
#    Type Text    text=Password    ${password}
#
#Submit Credentials
#    Click    input[type=submit]
#
#Welcome Page Should Be Open
#    # Example of using inline operators in tests
#    Get Url   ==   ${DEMO URL}
#    Get Text   body   ==   I salute you, Robot overloard!
#    Get Title  ==    Robots rule
