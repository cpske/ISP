# Python decorators.
# See: https://python-textbok.readthedocs.io/en/1.0/Functions.html#decorators

# Default log file for messages
import sys
logfile = sys.stdout


def print_decorator(fun):
    """
    Print calls to a function. 

    Argument: 
        fun - a function to decorate
    Returns:
        a new function that adds printing to the original function
    """
    def new_fun(*args, **kwargs):
        args_str = ",".join(str(arg) for arg in args)
        print(f"calling {fun.__name__}({args_str})")
        result = fun(*args, **kwargs)
        print("return", result)
        return result

    return new_fun


# You can apply a decorator just by annotating a function definition:
@print_decorator
def greet(name: str):
    print("Hello,", name)


if __name__ == '__main__':
    greet("SKE Nerds")

    import math

    # decorate a function using code
    f = print_decorator(math.sqrt)
    y = f(7)
    print("sqrt of 7 is ", y)
    print("sqrt of 500 is ", f(500))

    logmax = print_decorator(max)
    z = logmax(5, 99, -1000)
    print("max(5,99,-1000) is ", z)

