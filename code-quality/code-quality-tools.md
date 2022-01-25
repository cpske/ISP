---
title: Tools to Check Code Quality
---

Tools can check coding style and possible code problems, such as semantic errors or use of undefined variables. They are called "linters", "static analyzers", or "code auditors".  

The name "lint" comes from the classic `lint` tool for C-language programs. 

Tools can find:

1. Coding Problems
   - language violations
   - unused variables and unused imports
   - variables used before assignment
   - possible unintended behavior
   - dangerous code
2. Style Problems
   - violation of coding style convention
   - violation of commenting convention
   - inconsistent coding style


## Coding Quality Tools

"[*Python Code Quality: Tools & Best Practices*][real-python-code-quality]"
article in [Real Python][real-python-code-quality] discribes the benefits of code analysis and what teach tools does.

The top tools for Python are:

* [Pylint](https://www.pylint.org/) one of the most widely used tools.  Checks for style using PEP8 guidelines and looks for bad code signs.  
  - Checks code style and possible problems
  - Assigns **quality score** to your code
  - Can configure to ignore some items or some parts of code (.pylintrc)
  - Can create UML class diagrams
  - Don't expect to eliminate all warnings
  - Install: `pip install pylint`
  - Usage: `pylint path_to_code`  (one or more file names or directory name)

* [Flake8](http://flake8.pycqa.org/en/latest/) combines 3 tools:
  - PyFlakes - finds errors and potential code problems
  - pycodestyle - checks coding style using a subset of PEP8
  - Mccabe - checks McCabe complexity of code
  - Install: `pip install flake8`
  - Flake8 has many plugins, including a [Django plugin](https://pypi.org/project/flake8-django/)

* [MyPy](http://mypy-lang.org/) static type checking using type hints
  - [Code examples](http://mypy-lang.org/examples.html) on Mypy home, side-by-side examples of using type hints

* [Pydocstyle](http://www.pydocstyle.org/en/stable/) tool to check that docstring comments match the PEP257 standard.  Very useful!
  - if you use flake8, add this to flake8: `pip3 install flake8-pydocstrings`
  - otherwise, install it as stand-alone tool: `pip3 install pydocstyle`

* [Pylama](https://github.com/klen/pylama) A wrapper for 9 different tools, including the tools in Flake8.
  - not as popular as the above tools

* This [Github repo][github-code-analysis-tools] has more details and even more tools.

## Running pylint or flake8

You run pylint or flake8 on a file(s) or package (directory). It will show several messages with line numbers:
```bash
> pylint bank_account.py

bank_account.py:1:0: C0114: Missing module docstring (missing-module-docstring)
bank_account.py:104:12: R1720: Unnecessary "else" after "raise" (no-else-raise)
bank_account.py:139:29: W1309: f-string does not have ... (f-string-without-interpolation)
```

The line number is printed after the filename. C0114, R1720, etc. are message codes.    
The first letter in the message code is a category:

**C** convention. Violation of coding convention.    
**D** documentation. Violation of documentation standard.    
**R** refactor. Suggest refactor based on "good practice" metric violation.    
**W** warning for stylistic problem or minor programming issue.
**E** error.  Code that is probably an error.    
**F** fatal. Error that prevents Pylint from continuing


When you run flake8 the output will look like:
```bash
> flake8 bank_account.py

bank_account.py:17:1: W293 blank line contains whitespace
bank_account.py:20:28: E999 SyntaxError: invalid syntax
bank_account.py:23:69: E226 missing whitespace around arithmetic operator
bank_account.py:26:1: W293 blank line contains whitespace
bank_account.py:28:43: W292 no newline at end of file
```

You can customize what pylint and flake8 report. (See sections below.)
But don't overdo it and don't be lazy!  Better to fix your code than 
customize the tool to ignore some problems.

## Code Analysis in your IDE

All IDE do some code quality checking automatically.  You can also add
more checking as described here:

**VS Code** 
- The VS Code "Language Server" performs style and code checking, but you can add an external linter.
- Press Control+Shift+P and enter "Python Select Linter" to choose a "Lint" tool.  
- After you enable linting, it is run automatically whenever you save a file or when you enter Control+Shift+P and type/choose "Python: Run Linting"
- How to: <https://code.visualstudio.com/docs/python/linting>

**Pycharm**
- Has an extensive builtin code checker. In the "Problems" window (lower part of default IDE layout) it includes style and code problems, as well as errors.
- How to Configure Code Style: <https://www.jetbrains.com/help/pycharm/configuring-code-style.html#configure-code-style-schemes>
- You can add **flake8** or **pylint** as "External Tools". 
- See: <https://www.jetbrains.com/help/pycharm/configuring-third-party-tools.html>

**Pydev** (Eclipse Plugin)
- Includes "Code Analysis" feature that uses Pylint.
- Configure it in Preferences -> Pydev -> Code Analysis    
  - I had to manually specify the location of `pylint` for it to work.  
- Run it: Right-click on a file and select Pydev -> Code Analysis.
- Problems are shown as warning/error markers in left margin of
  editor window.  Will also show in Console if you check this preference:    
  [x] Redirect Pylink output to console?


### Customize Pylint 

Pylint looks for a configuration file in your current directory and your home directory. Or, you can specify one using the `--rcfile filename` command line option.  In order of priority:

* File given using a `--rcfile filename` command line options
* `pylintrc` or `.pylintrc` in current dirctory
* file named by the `PYLINTRC` environment variable
* `.pylintrc` or `config/.pylintrc` in your home directory

An example pylintrc file is:
```
[MESSAGES CONTROL]
disable = C0102   # ignore black-listed name, such as 'foo'

```
To see **everything** you can set in pylintrc (it's long), run:
```
pylint --gen-rcfile > example.pylintrc
```

Run Pylint and also print a detailed report:

```shell
pylint -ry filaname.py
```

### Customize Flake8

Flake8 can have both a per-project config file and a global config file.

* Project Configuration: a file named `setup.cfg`, `tox.ini`, or `.flake8` in the project top-level directory
* Global Configuration: a file `$HOME/.config/flake8` on Linux and MacOS. On Windows, file `.flake8` in your home directory.
* Command Line Options override options in a configuration file

An example of a Flake8 config for Django. 
This allows longer lines (default 79) and only 1 blank line between top-level functions.

```
[flake8]
# Django recommends allowing longer lines, such as in models
max-line-length = 119
# test docstrings using PyFlakes
doctests = True

exclude =
    # excluded by default
    .git,
    __pycache__,
    # ignore virtual environments (not our code)
    env,
    venv,
    # Useless to check autogenerated migrations files.
    migrations
```

You should **fix** violations, **not** ignore them.  
So, do not write this:
```
[flake8]
ignore =
    C111    # missing docstring
    C303    # trailing whitespace
    E302    # expected 2 blank lines, found 1
    F401    # import not used
    ...
```
OK to include a very small number of ignores if you have a **good reason**.    
All the above example codes are easy to fix, so no reason to ignore them.


See [Configuring Flake8](https://flake8.pycqa.org/en/latest/user/configuration.html) and [List of Options](https://flake8.pycqa.org/en/latest/user/options.html)


### Checking Django Projects

There are plugins for better analysis of Django projects:

* [pylint-django](https://pypi.org/project/pylint-django/) 
  - Installation: `pip install pylint-django`
  - Usage:  `pylint --load-plugins pylint_django path_to_source_code`

* [Flake8 Django plugin](https://pypi.org/project/flake8-django/) 
  - Installation: `pip install flake8-django`
  - Usage: `cd django-project; flake8`
  - flake8 automatically uses the plugin. In my test, it needs some extra configuration to eliminate superfluous messages.

## Check Style for Java

Java is a statically typed, compiled language. A Java IDE and compiler perform a lot of checks for syntax and semantic errors, hence there is less work for other tools.  Some examples of this are:

* A variable must always be declared (avoids spelling errors in variable names).
* Java won't let you use a local variable before a value is explicitly assigned. 
* Attributes are assigned a default value (null, zero, or false) but the IDE and compiler will warn you if it looks like you are using an attribute before explicitly assigning a value.
* Compiler and IDE both warn if you don't close a locally created resource, like a Scanner or InputStream.
* Compiler won't let you pass the wrong type as a parameter or return the wrong type from a method.

For code style checking the standard tool is [Checkstyle](https://checkstyle.sourceforge.io) and [Checkstyle on Github](https://github.com/checkstyle/checkstyle).  It can be integrated into any IDE, even BlueJ.

* [Using Checkstyle](https://skeoop.github.io/docs/Checkstyle.pdf) from Programming 2
* KU Checkstyle Rules [ku-checkstyle.xml](https://skeoop.github.io/docs/ku-checkstyle.xml) by Thai Pangsakulyanont. The rules define the coding standard that Checkstyle expects.

## Resources

[Python Code Quality: Tools & Best Practices][real-python-code-quality] article on Real Python with description of many tools, and code example.

[Python Linters and Code Analysis Tools Curated List][github-code-analysis-tools] detailed list of tools with description and recommendations.

[Flake8](https://simpleisbetterthancomplex.com/packages/2016/08/05/flake8.html) on SimpleIsBetterThanComplex.com has good explanation of Flake8 outout, configuration, and example of testing a Django project with Flake8 and coverage on Travis-CI.

[real-python-code-quality]: https://realpython.com/python-code-quality/
[github-code-analysis-tools]: https://github.com/vintasoftware/python-linters-and-code-analysis
