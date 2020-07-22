---
title: Feedback on Selenium Testing
---

### Good Testing Code

Kornphon, Supalak, and Vichaphol wrote test code like this:

```python
def main(url):
    links = get_links(url)
    for link in links:
        print(link)

    invalid_links = invalid_urls(links)
    print('Invalid URLs:')
    for link in invalid_links:
        print(link)

if __name__ == "__main__":
    # Code to run if this file is run as a script
    main( 'https://cpske.github.io/ISP/' )
```

This is the way you **should** write Python. Very good!

> If they had written **docstring** comments 
> on *all* methods (as Kunyarak did) it would be really Professional code.

In Python, `__name__` is an automatic global variable.
If a file is executed as a module, such as by using `import module` 
and invoking a function in the file, then `__name__` is the name of the module.

If a file is being directly interpretted by Python, such as when you run
`python filename`, then `__name__` is `"__main__"`.

If your file has code you want to run as the "main method" (like in Java), 
put it inside an `if __name__ == "__main__"` block as in the above example.

The benefit is that your file can be run as either a script or a module.

### Something Missing?

In the above example code, is anything missing?
Imagine what the output will look like in all cases.

### Common Mistakes

Since this is a course about good software process,
I deducted 0.2 points for not following the assignment specification.
Common mistakes were:

* not putting test code in a `main()` function 
* incorrect function names

Both of these mean that I have to edit your file before it can be tested using `unittest`.
