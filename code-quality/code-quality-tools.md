---
title: Tools to Check Code Quality
---

Tools can check coding style and possible code problems, such as semantic errors or use of undefined variables. They are called "linters", "static analyzers", or "code auditors".  "Lint" comes from the `lint` tool for C-language programs. 

Tools can find:

1. Coding Problems
   - language violations
   - unused variables
   - variables used before assignment
   - possible unintended behavior
   - dangerous code
2. Style Problems
   - violations of coding style convention
   - violations of commenting convention
   - inconsistent coding style

## Coding Style and Code Analysis Tools

"[*Python Code Quality: Tools & Best Practices*][real-python-code-quality]"
article in [Real Python][real-python-code-quality] discribes the benefits of code analysis and what teach tools does.

This [Github repo][github-code-analysis-tools] has more details and even more tools.

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

* [Pylama](https://github.com/klen/pylama) A wrapper for 9 different tools, including the tools in Flake8.
  - not as popular as the above tools

### Checking Django Projects

There are plugins to provide better analysis and checking of Django projects:

* [pylint-django](https://pypi.org/project/pylint-django/) 
  - Installation: `pip install pylint-django`
  - Usage:  `pylint --load-plugins pylint_django path_to_source_code`

* [Flake8 Django plugin](https://pypi.org/project/flake8-django/) 
  - Installation: `pip install flake8-django`
  - Usage: `cd django-project; flake8`
  - flake8 automatically uses the plugin. In my test, it needs some extra configuration to eliminate superfluous messages.
  - see Flake8 documentation for how to create a config file, either (Windows) `.flake8` or (Linux/MacOS) `.config/flake8`

[Flake8](https://simpleisbetterthancomplex.com/packages/2016/08/05/flake8.html) on SimpleIsBetterThanComplex.com has good explanation of Flake8 outout, configuration, and example of testing a Django project with Flake8 and coverage on Travis-CI.

## Code Analysis in your IDE

* VSCode - Control-Shift-P and enter "Python Select Linter", then Control-Shift-P and "Python Run Linter".
* Pycharm has its own build-in code checker which constantly suggests improvements. 
  - To run Code Analysis, from menu select Code-&gt;Inspect Code... and choose file(s) to inspect.
  - output is shown in "Inspection Results" panel at bottom.  Click on an item to go to source line.
  - offers suggested code change in another panel
* Pydev (Eclipse) has "Code Analysis" feature that uses Pylint.
  - Configure it in Preferences -> Pydev -> Code Analysis    
    I had to manually specify the location of `pylint` for it to work.  
  - Right-click on a file and select Pydev -> Code Analysis.
  - Problems are shown as warning/error markers in left margin of
    editor window.  Will also show in Console if you check preference:    
    [x] Redirect Pylink output to console?

## Resources

[Python Code Quality: Tools & Best Practices][real-python-code-quality] article on Real Python with description of many tools, and code example.

[Python Linters and Code Analysis Tools Curated List][github-code-analysis-tools] detailed list of tools with description and recommendations.

[Flake8](https://simpleisbetterthancomplex.com/packages/2016/08/05/flake8.html) on SimpleIsBetterThanComplex.com has good explanation of Flake8 outout, configuration, and example of testing a Django project with Flake8 and coverage on Travis-CI.

[real-python-code-quality]: https://realpython.com/python-code-quality/
[github-code-analysis-tools]: https://github.com/vintasoftware/python-linters-and-code-analysis
