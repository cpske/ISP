## Checking Code Quality

## Style Guide and Coding Convention

For coding style, start with these standards:

1. [pep8.org](http://pep8.org/) is a single page easy-to-read summary of how to use [PEP 8](https://www.python.org/dev/peps/pep-0008/) the official Python Style Guide.
2. Python Guide for Docstrings [PEP 257](https://www.python.org/dev/peps/pep-0257/)
3. [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
    - Part 2 is guidelines for using the Python language 
    - Rule #1 is "run `pylint` over your code"!
    - Part 3 "Python Style Rules" are rules for coding style
    - Part 4 "Parting Words" is *Be Consistent*
    - Google's guide is very prescriptive (do and don't) on how to write code.

## Tools to Check Your Code

Tools can check for coding style and possible code problems. They are called "linters","code analyzers", or "code auditors".  "Lint" comes from the `lint` tool for C-language programs.  Pycharm and Pydev provide *some* of this by default.

Tools can find:

1. Coding Problems
    - language violations
    - unused variables
    - possible unintended behavior
    - dangerous code
2. Style Problems
    - violations of coding style convention
    - violations of commenting convention
    - inconsistent coding style

## Coding Style and Code Analysis Tools

An [article in Real Python][real-python-code-quality] discribes many code analyzers and what each one does.
This [Github repo][github-code-analysis-tools] has more details and even more tools.

A few good ones are:

* [Pylint](https://www.pylint.org/) one of the oldest and most widely used.  Checks for style using PEP8 guidelines and looks for bad code signs.  Needs some configuration to avoid extraneous messages.
    - Checks code style and possible problems
    - Assigns **quality score** to your code
    - Can configure to ignore some items or some parts of code
    - Can create UML class diagrams
    - Don't expect to eliminate all warnings
    - Install: `pip install pylint`
    - Usage: `pylint path_to_code`  (one or more file names or directory name)

* [Flake8](http://flake8.pycqa.org/en/latest/) combines 3 tools:
    - PyFlakes - finds errors and potential code problems
    - pycodestyle - checks coding style using a subset of PEP8
    - Mccabe - checks McCabe complexity of code
      
* [Pylama](https://github.com/klen/pylama)
    - A wrapper for 9 different tools, including the tools in Flake8

For Pylint-ing Django projects:

* [pylint-django](https://pypi.org/project/pylint-django/) a plugin for pylint to improve checking of Django projects.
    - Installation: `pip install pylint-django`
    - Usage:  `pylint --load-plugins pylint_django path_to_source_code`

## Use Code Analysis in your IDE

* VSCode - Control-Shift-P and enter "Python Select Linter", then 
     Control-Shift-P and "Python Run Linter".
* Pycharm has its own build-in code checker which constantly suggests improvements. 
    - To run Code Analysis, from menu select Code->Inspect Code... and choose file(s) to inspect.
    - output is shown in "Inspection Results" panel at bottom.  Click on an item to go to source line.
    - offers suggested code change in another panel
* Pydev has "Code Analysis" feature that uses Pylint.
    - Configure it in Preferences -> Pydev -> Code Analysis    
      I had to manually specify location of `pylint` for it to work.  
    - Right-click on a file and select Pydev -> Code Analysis.
    - Problems are shown as warning/error markers in left margin of
      editor window.  Will also show in Console if you check preference:    
    [x] Redirect Pylink output to console?

## Resources

[Python Code Quality: Tools & Best Practices][real-python-code-quality] article on Real Python with description of many tools.

[Python Linters and Code Analysis Tools Curated List][github-code-analysis-tools] detailed list of tools with description and recommendations.

[real-python-code-quality]: https://realpython.com/python-code-quality/
[github-code-analysis-tools]: https://github.com/vintasoftware/python-linters-and-code-analysis
