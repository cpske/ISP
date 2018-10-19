### Project 

During first iteration:

- Experimentation.
- Set up test, CI, deploy tooling early.
- Identify what's risky and attack it first.
- Create a simple proof of concept.

Advise for Chat, OWSA:

- Do performance (load) testing.  Don't try to optimize.

Thai's App, from his senior project at KU: [Bemuse](github.com/bemusic/bemuse).
- Its open source and has several contributors.
- He applies CI, auto deployment, E2E testing
- Uses Amplitude for analytics.

## Coding

Prettier.io formatter for Javascript.

Code Clinic - Github addon.  Analyzes your code after each commit.

ESLint

[PyLint](https://www.pylint.org/) for Python.

Using PyLint in VSCode (from VSCode Documentation):
  1. Enter Control-Shift-P to open command palette.
  2. Choose "Python Select Linter".  Choose pylint.
  3. VS Code prompts to install PyLint if not already installed.
  4. Linting runs automatically when you save a Python file.
     To manually run it, use

VS Code - read the best practices for Python!

Linter for English - https://github.com/btford/write-good

## Good Example Projects

[Visual Studio Code](https://github.com/Microsoft/vscode) - has lots of info in wiki.  Has iteration plans.

### Testing

Practical Test Pyramid on MartinFowler.com

1. End to End (E2E) Tests
2. Integration Tests
3. Unit Tests

Tools:

* Prescript - test runner
* Puppeteer - Google in-browser tester. 
* Selenium - another tester, used at TaskWorld.
* Mocha, Chai - test tools

### Code Coverage

Shows how much code is exercised by tests.

### Automatic Deployment

Deploy to preview site.

### Communication

Majority of project failures are due to people problems.

Always connecting with goals.

### For Web Apps, how to you keep track of routes, URLs, and their purpose?

Thai relies on the code.  Three levels of disagregation of routes:

1. Central routing file
2. Dist'd routing file, like "apps" in Django
3. Dynamic routing using a Registry
