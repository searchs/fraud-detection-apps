import time

from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time of {func.__name__}: {end-start} seconds")
        return result

    return wrapper


# @timer Examples
@timer
def factorial(n):
    """Returns the factorial of n"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


@timer
def fibonacci(n):
    """Returns the nth Fibonacci number"""
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(factorial(10))
print(fibonacci(10))


def debug(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(
            f"Calling {func.__name__} with args: {args} and kwargs: {kwargs}"
        )
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result

    return wrapper


# @debug Examples
@debug
def add(x, y):
    """Returns the sum of x and y"""
    return x + y


@debug
def greet(name, message="Hello"):
    """Returns a greeting message with the name"""
    return f"{message}, {name}!"


print(add(2, 3))
print(greet("Alice"))
print(greet("Bob", message="Hi"))

# Caching Results


def memoize(func):
    cache = {}

    @wraps(func)
    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            return result

    return wrapper


# @memoize Example
@memoize
def factorial(n):
    """Returns the factorial of n"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


@memoize
def fibonacci(n):
    """Returns the nth Fibonacci number"""
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(factorial(10))
print(fibonacci(10))
