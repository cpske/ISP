## Robot Framework

[Robot Framework](https://robotframework.org) is an
"automation framework" for testing and robotic process automation (RPA).
It uses an extensible English-like grammar.

## Install and Run Robot Framework

Instruction to install and learn it are at [Getting Started](https://robotframework.org/#getting-started) page.

To install the framework *and* selenium library for browser-based web testing:
```shell
   pip install robotframework
   pip install robotframework-seleniumlibrary
```

## Usage & Example 

1. Write your robot script in a file with extension `.robot`.

2. The file is divided into sections (`Settings`, `Variables`, `Keywords`, `Tests` or `Tasks`).

3. Each section begins with asterisk `*` but typically 3 asterisks `***` are used, e.g. `*** Settings`.

4. **Keywords** are instructions. They are actually multi-word phrases such as `Get Length` (Builtin keyword), `Page Should Contain` (Selenium library), or your own defined keywords.

5. **Space Between Arguments**: because keywords are actually phrases (with 1 space between words), you must leave **at least 2 spaces** between the "keyword" and its argument, and usually 2 spaces between arguments.

6. Refer to variables using `${variableName}` like in the Bash shell language.

Example: `visitcpe.robot`

```robot
*** Settings ***
Documentation     View the CPE Homework using a Web Browser
Library           SeleniumLibrary

*** Variables ***
${SITE_URL}       https://www.cpe.ku.ac.th
${BROWSER}        Firefox

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
```

Run it: `robot visitcpe.robot` or `python -m robot visitcpe.robot`

The test fails because the "Location Should Be" doesn't exactly match the actual URL.  That can be fixed.  Nonetheless, it shows how to write a test.

Robot creates 3 output files:
- output.xml
- log.html
- report.html

The `report.html` contains a detailed report of your tests.

You can specify filenames or suppress creation of each of these files using the -o -l and -r options:
```
robot -o NONE -l NONE -r cpereport.html  visitcpe.robot
```


### Robot Framework Standard Libraries

[Standard Libraries](http://robotframework.org/robotframework/#standard-libraries) are where all the "keywords" used in your scripts are defined.
These are included with the framework:

- [BuiltIn][] provides standard "keywords" like "should equal", logs
- [Collections][] provides keywords for using Python lists, collections, and dictionaries, such as "append to ..." or "get from dictionary", "list should contain ...".
- [DateTime][] keywords for getting date/time and testing date/times
- [Dialogs][] keywords for interacting with the user
- [OperatingSystem][] keywords for using operating system commands such as "run" to run a command, create and remove files and directories, check file existences or check a file contains a value
- [Process][] keywords for running processes; "run process", "start process" (run in background), wait for, stop processes
- Remote is part of the [remote library interface][remote-library]
- [Screenshot][] keywords to take a screenshot of application
- [String][] keywords for string manipulation, including regular expressions, split string into lines, verifying string contents
- [Telnet][] keywords for a connection over telnet (really? Telnet is insecure and deprecated. Probably uses SSH)
- [XML][] keywords for working with XML files or XML data

[BuiltIn]: http://robotframework.org/robotframework/latest/libraries/BuiltIn.html
[Collections]: http://robotframework.org/robotframework/latest/libraries/Collections.html
[DateTime]: http://robotframework.org/robotframework/latest/libraries/DateTime.html
[Dialogs]: http://robotframework.org/robotframework/latest/libraries/Dialogs.html
[OperatingSystem]: http://robotframework.org/robotframework/latest/libraries/OperatingSystem.html
[Process]: http://robotframework.org/robotframework/latest/libraries/Process.html
[Screenshot]: http://robotframework.org/robotframework/latest/libraries/Screenshot.html
[String]: http://robotframework.org/robotframework/latest/libraries/String.html
[Telnet]: http://robotframework.org/robotframework/latest/libraries/Telnet.html
[XML]: http://robotframework.org/robotframework/latest/libraries/XML.html
[remote-library]: https://github.com/robotframework/RemoteInterface

These libraries mostly provide an interface between RF's keyword language and Python libraries.

Other libraries (you have to install them yourself):

- [SeleniumLibrary][selenium-library] a browser control library using Selenium.
- [Browser Library][browser-library] control a web browser, test elements on a page, click elements. 
- [Browser](https://marketsquare.github.io/robotframework-browser/Browser.html) Keywords reference with explanation

I use only SeleniumLibrary.

### Robot Framework Standard Tools

- Testdoc
- Tidy
- Libdoc
- Robot

## Resources

[browser-library]: https://robotframework-browser.org/
[selenium-library]: https://robotframework.org/SeleniumLibrary/SeleniumLibrary.html

[Getting Started](https://robotframework.org/#getting-started) how to install, examples, and links to some tutorials.

[QuickStart](https://github.com/robotframework/QuickStartGuide/blob/master/QuickStart.rst) the syntax with examples and some Python code (on Github). I didn't find it very useful.

[User Guide](http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html) is more useful.

[Standard Libraries](http://robotframework.org/robotframework/#standard-libraries) links to the Keyword reference for each of the standard libraries. Useful for constructing tests.

[SeleniumLibrary](https://robotframework.org/SeleniumLibrary/) complete introduction to this library.

[SeleniumLibrary Keywords](https://robotframework.org/SeleniumLibrary/SeleniumLibrary.html) single page reference for the keywords.

"Basic Concepts of Robot Framework" with focus on RPA.
<https://robocorp.com/docs/languages-and-frameworks/robot-framework/basics>


## Using SeleniumLibrary in a Test

```robot
*** Settings ***
Documentation   Some test using seleniumlibrary
Library         SeleniumLibrary
Resource        mytests.resource

*** Variables ***
# variable names can contain spaces
${LOGIN URL}    https://localhost:8000/accounts/login/
${BROWSER}      Firefox
@{LISTVAR}      first   second   third   fourth
&{DICTVAR}      username=harry   password=hacker  email=harry@hackerone.com

*** Test Cases ***
Valid Login
	Open Browser to Login Page
	Input Username   demouser
	Input Password   demopass
	Submit

*** Keywords ***
# User-defined keywords (actions & expressions)

Open Browser to Login Page
    Comment this is a comment that is included in the output
	Open Browser  ${LOGIN URL}  ${BROWSER}

Input Username
	[Arguments]  ${username}
	Input Text	 usernamefield  ${username}
    # use  id:   or   name:  to specify search criterion
    Input Text   name:usernamefield  {$username}

Input Password
	[Arguments]  ${password}
	Input Text	 passwordfield  ${password}

Submit
	Click Button   login_button
    # or use the button class (if there is only 1 "submit" on the page)
    Click Button   class:submit

*** Tasks ***
# User defined tasks

```

Complete example of login test using SeleniumLibrary:
<https://www.edureka.co/blog/robot-framework-tutorial/>.
(This is actually copied from other sources.)
