### Logging Exercise: Logging Function Calls

Logging function calls can help you understand a part of a code.

Here's a function that uses recursion to find integer factors
of a number.

It uses `print` statements to show calls and returns.
Makes the function hard to read, right?  And we eventually
need to remove those print statements.

```python
def factor(n):
    """Return the prime factors of n, including 1.  n must be a positive integer."""
    print("factor({0})".format(n))
    if n == 1:
        print("return [1]") 
        return [1]
    if n < 1:
        raise ValueError("must be positive integer")
    for f in range(2, n):
        if n % f == 0:
            result = [f] + factor(n//f)
            print("return", result)
            return result
    # is something missing here? Fix it.
    return [n]

if __name__ == '__main__':
    for n in [36, 37, 110, 240000]:
        print(f"factor(n) = ")
        print(factor(n))
```

Try calling it to see how it works.

### Starter Code

```python
import logging

def config():
    """configure the logger"""
    root = logging.getLogger()
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    root.addHandler(log)
    root.setLevel(logging.DEBUG)
```

