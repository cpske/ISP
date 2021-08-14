---
title: Project Documentation
---

You need documentation for users of your application, including: 

* installation instructions (if any)
    - including list of requirements
* getting started
    - including supported environments, such as OS or web browsers
* user guide
    - this can also be referenced by your web app as links

For programmers you need

* API reference

API docs for present and future developers.

Use Python docstring comments to create API docs. Sphinx is a good tool.

* Vision statement
* Software design document and architecture notes

## Documentation Tools

* [Swagger](https://swagger.io) for online API documents.  Swagger is especially popular for REST APIs.
* [Sphinx](https://sphinx-doc.org) for all kinds of documents.  Sphinx uses Restructured Text (rst) as the markup language in documents.  It can create API docs from docstring comments in Python source code.
* Rhinotype or LaTeX are invoked by Sphinx or other tools to generate book-quality PDFs.

[readthedocs.org](https://readthedocs.org) can host and generate your project docs using Sphinx.  


## Using Sphinx to create Project Documentation

You must install Sphinx first.

> *Don't put Sphinx output in your project root dir.*
> 
> Sphinx output will pollute your source tree.
> Use a separate directory, e.g. `docs` subdirectory.
> You need to edit Sphinx-generated `conf.py` to specify
> the project base directory, as shown below.

1. In the project directory run `sphinx-quickstart`.  This command asks questions about what to document and where.
```
project_dir$  sphinx-quickstart

> Root path for documentation [.]:
> Separate source and build directories (y/N)?  Y
> Name prefix for templates and static dir [_]?
> Project name to use in documentation? Todo Lists (avoid appending "Project")
> Author name(s):
> Project release [1.0]:
> Source file suffix [.rst]:
> Name of master document (without suffix) [index]:
> Automatically insert docstrings from modules (y/N)? y   (choose "y") 
> Test code snippets in doctest blocks (y/N)? n
> inersphinx: Link to Sphinx docs in other projects (y/N)? n
> todo: write "todo" entries that can be shown or hidden in build (y/N)? n
> coverage: check for documentation coverage (y/N)? n
> pngmath: include math, rendered as PNG images (y/N)? n
> jsmath: include math rendered in borwser by JSMath (y/N)?
> ifconfig: conditional includsion of content based on config values (y/N)? n

A Makefile can be generated for you so that you only need
to run "make html" instead of invoking sphinx-build directly.

> Create Makefile (Y/n)?  y
> Create Windows command file (Y/n)?  n (choose "y" if using windows)
```
2. After sphinx-quickstart runs, edit `index.rst` and add content about your projects.
3. For code, you need to tell Sphinx where the code is.  Edit `conf.py`.

### Stupid! (Should be done automatically) Add Extensions to conf.py

```python
extensions = [
    'sphinx.ext.autodoc',  # generate docs from python code
    'sphinx.ext.todo',
    'sphinx.ext.viewcode'
]
```

### Running Sphinx

```
make clean
make html
```

### Sphinx Video Tutorials

* https://www.youtube.com/watch?v=LQ6pFgQXQ0Q (9 minutes)
