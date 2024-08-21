# decorators - We used them as Toll plaza

import time
def decor(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in time {end - start} s")
        return result
    return wrapper


@decor
def example_function(n):
    time.sleep(n)

example_function(2)
