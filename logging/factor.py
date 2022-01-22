"""
Example of using a log decorator to "wrap" a function
so we can log calls and returns for that function.
"""


def log_decorator(fun):
    """Define a decorator (wrapper) for fun that logs function calls."""
    def wrapped_fun(*args, **kwargs):
        # print the function call in format fun_name(arg1,...)
        argstring = ','.join(str(arg) for arg in args)
        print(f"{fun.__name__}({argstring})")
        ret = fun(*args, **kwargs)
        print(f"{ret}")
        return ret
    # return a function
    return wrapped_fun


@log_decorator
def factor(n):
    """Return the prime factors of n, using recursion.  
       n must be a positive integer.
    """
    print(f"factor({n})")
    if n == 1:
        print("return [1]") 
        return [1]
    if n < 1:
        raise ValueError("param must be positive integer")
    # really stupid way of finding prime factors
    for f in range(2, n):
        if n % f == 0:
            result = [f] + factor(n//f)
            print(f"return {result}")
            return result
    result = [n]
    print(f"return {result}")
    return result


if __name__ == "__main__":
    n = 1
    while n > 0:
        n = int(input("Integer to factor: "))
        if n == 0: break
        factors = factor(n)
        print(f"Factors of {n} are {factors}")
