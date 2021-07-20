from functools import lru_cache


def factorial(n):
    if n > 1:
        return n * factorial(n - 1)
    else:
        return 1


@lru_cache
def factorial_cache(n):
    if n > 1:
        return n * factorial(n - 1)
    else:
        return 1
