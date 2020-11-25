# Python decorators.
# See: https://python-textbok.readthedocs.io/en/1.0/Functions.html#decorators

# Default log file for messages
import sys
logfile = sys.stdout


def log_decorator(fun):
    """
    Add logging to each function call.
    Parameters:
        :fun: a function to decorate
    Returns:
        the original function wrapped in a logging decorator
    """
    def new_fun(*args, **kwargs):
        logfile.write("calling %s%s, kwargs=%s\n" % (fun.__name__, args, kwargs))
        return fun(*args, **kwargs)

    return new_fun

# You can apply a decorator just by annotating a function definition:
@log_decorator
def greet(name: str):
    print("Hello,", name)


if __name__ == '__main__':
    greet("SKE Nerds")

    import math

    # decorate a function using code
    f = log_decorator(math.sqrt)
    y = f(7)
    print("sqrt of 7 is ", y)
    print("sqrt of 500 is ", f(500))

    logmax = log_decorator(max)
    z = logmax(5, 99, -1000)
    print("max(5,99,-1000) is ", z)

