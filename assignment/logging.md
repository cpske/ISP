### Logging Exercise

Add logging to the following code for recursively computing prime factors.

1. Print a DEBUG level log message each time factor(n) in entered and before it returns.
2. Print an ERROR level message if it is invoked with invalid argument.
3. Remove all the `print` statements.
4. Use the following log format and log to the console.

```
2018-11-22 14:30:00 factor INFO factor(6)
2018-11-22 14:30:01 factor INFO factor(3)
2018-11-22 14:30:02 factor INFO factor(2)
2018-11-22 14:30:03 factor INFO return [2]
2018-11-22 14:30:04 factor INFO return [2,3]
2018-11-22 14:30:05 factor INFO return [1,2,3]
2018-11-22 14:30:06 factor ERROR Invalid argument "one"
```

### Starter Code

```python
import logging

def config():
    """configure the logger"""
    pass

def test():
    log = logging.getLogger('factor')
    log.info("an info message")
    log.warning("a warning")
    log.error("an error")

def factor(n):
    """Return the prime factors of n.  n must be a positive integer."""
    print("factor({0})".format(n))
    if n == 1:
        print("return [1]") 
        return [1]
    if n < 1:
        raise ValueError("must be positive integer")
    for f in range(2, n):
        if n % f == 0:
            result = [f] + factor(n//f)
            print("return {}".format(result))
            return result
    # something missing?
    return [n]

if __name__ == '__main__':
     """Write some code here"""
     config()
     print("factor(36) = ", factor(6))
```

### What to Submit

Don't need to submit this.
