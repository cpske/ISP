"""
Compute the factors of an integer using recursion.

TODO: 
  1. Replace "print" statements with logging, using appropriate log levels.
  2. Direct the log output to a file, so it doesn't interfere with the console
     dialog that the user sees.
  3. In main, catch & log the exception with a stacktrace. The user should not see the stacktrace on the console.
"""


def factor(n):
    """Return the prime factors of n, using recursion.  

       :param n: a positive integer to factor
       :returns: list of prime factors of n
       :raises TypeError: if n is not an integer
       :raises ValueError: if n is not a positive integer
    """
    print(f"factor({n})")
    if n == 1:
        print("return [1]") 
        return [1]
    if not isinstance(n, int):
        print(f"Error: factor({n}) parameter not an int")
        raise TypeError("parameter must be an int")
    if n < 1:
        print(f"Error: factor({n}) parameter not a positive int")
        raise ValueError("parameter must be positive integer")
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
        try:
            n = int(input("Integer to factor: "))
        except Exception as e:
            print(e)
            print("Please input an integer value")
            continue
        if n == 0: break
        factors = factor(n)
        print(f"Factors of {n} are {factors}")
