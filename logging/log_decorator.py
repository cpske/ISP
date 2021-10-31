"""
A function decorator to perform logging.

See: https://python-textbok.readthedocs.io/en/1.0/Functions.html#decorators
"""


def log_decorator(fun):
    """A decorator for a function that logs each function call
       and the return value.

       The simplest way to use this decorator is as
       an annotation in front of the function to decorate:
       @log_decorator
       def your_function(...)

       Arguments:
           fun - a function to wrap.
       Returns:
           a decorated function that invokes fun
    """
    def wrapped_fun(*args, **kwargs):
        # log the function call in format fun_name(arg1,...)
        #print("%s%s, kwargs=%s\n" % (fun.__name__, args, kwargs))
        argstring = ','.join(str(arg) for arg in args)
        print(f"{fun.__name__}({argstring})")
        ret = fun(*args, **kwargs)
        if ret != None:
            print(f"return {ret}")
        else:
           print("return")
        return ret
    return wrapped_fun


@log_decorator
def greet(name):
    print("Hello,", name)

if __name__ == '__main__':
    greet("Nerd")

    import math

    # decorate a function using code
    f = log_decorator(math.sqrt)
    y = f(7)
    print("sqrt of 7 is ", y)
    print("sqrt of 500 is ", f(500))

    logmax = log_decorator(max)
    z = logmax(5, 99, -1000)
    print("max(5,99,-1000) is ", z)
