from itertools import combinations
from functools import partial, reduce
from operator import mul

mult = partial(reduce, mul)


def isqrt(n):
    from math import sqrt
    return int(sqrt(n))


def is_prime(long n):
    cdef long c, isqrt_n
    cdef int m

    if n < 2:
        return False
    if n < 4:
        return True
    if n & 1 == 0:
        return False
    if n % 3 == 0:
        return False

    isqrt_n = isqrt(n)
    c = 5
    m = 2
    while c <= isqrt_n:
        if n % c == 0:
            return False
        c += m
        m = 4 - m
    return True


def prime_factors(long n):
    cdef long c
    cdef int m

    while n & 1 == 0:
        n >>= 1
        yield 2

    while n % 3 == 0:
        n //= 3
        yield 3

    c = 5
    m = 2
    while c * c <= n and n != 1:
        while n % c == 0:
            n //= c
            yield c

        c += m
        m = 6 - m

    if n != 1:
        yield n

def all_factors(long n):
    factors = list(prime_factors(n))
    pairs = set([1])
    for i in range(1, len(factors) + 1):
        for comb in combinations(factors, i):
            pairs.add(mult(comb))
    return pairs

