---
title: Online Services with Badges
---

A good article on "*why badges?*": [Code Repository Badges](https://github.com/dwyl/repo-badges)
- it also shows *how* to create badges for docs, security, CI builds, test coverage, and Javascript "goodparts" (based on the book *Javascript: The Good Parts*).

## CI Services that Provide Badges

You might consider if these are useful for your project:

| URL                         | Used for            |
|:----------------------------|:--------------------|
| https://travis-ci.com       | build, test, deploy |
| https://appveyer.com        | Windows builds      |
| https://codeclimate.com     | maintainability, test coverage |
| https://codacy.com          | **code quality**    |
| https://inch-ci.org/        | **documentation quality** |
| https://codecov.io          | test coverage       |
| https://coveralls.io        | test coverage       |
| https://hakiri.io/          | security analysis   |
| https://snyk.io/            | security analysis   |
| https://gitter.im/          | chat channel        |

## Badge Services

[Shields.io on Github](https://github.com/badges/shields) and [Shields.io](https://shields.io) a site provides badges for various services.

[List of Badges in Markdown](https://github.com/Naereen/badges) many examples, mostly using shields.io.

Open Source Licenses: I suggest you do **not** attach a license to your project unless you read and agree to what the license actually states. To learn more, read the [Open Source License Comparison][open-source-licenses] and [ChooseaLicense.com](https://choosealicense.com).

[open-source-licenses]: https://en.wikipedia.org/wiki/Comparison_of_free_and_open-source_software_licenses


## Some Sites with Interesting Badges

* [Jekyll](https://github.com/jekyll/jekyll) has badges for Appveyer, Codeclimate, Hakiri, sponsors, Travis
* [VS Code](https://github.com/microsoft/vscode) has badges for Azure, Github open issues by category, chat on gitter
* [DBeaver](https://github.com/dbeaver/dbeaver) has badges for Codacy, Travis, Twitter, Github for Java CI
* [Checkstyle](https://github.com/checkstyle/checkstyle) has *ridiculous* number of badges.


## Self-hosted Services

### [SonarQube](https://www.sonarqube.org)

[SonarQube](https://www.sonarqube.org) is a scanner for code quality and security.  It was ranked No.1 in [7 Best Static Code Analysis Tools][7-best-tools].  The article also recommended Checkmarx, Snyk, and Reshift.

SonarQube Community Edition is free. You can download it as a Docker image or ZIP file of source.

[7-best-tools]: https://www.comparitech.com/net-admin/best-static-code-analysis-tools/


### Security Analysis Tools

[Top 12 Open Source Code Security Tools](https://spectralops.io/blog/top-12-open-source-code-security-tools/), an article by CheckPoint, 
recommends some tools to check for security issues in dependencies.
Some of the tools also perform static analysis of your code.

- Contrast OSS (commercial)
- Sprectral (their own product)
- WhiteSource (commercial)
- ShiftLeft Scan (free and open source)
- SonarQube (free community edition)
- Safety (free and open source) checks Python requirements.txt or virtual environments for security issues.  Github Dependabot does this.
- Snyk


