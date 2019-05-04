#!/usr/bin/env python3

from primes import is_prime, prime_factors, all_factors
from contextlib import contextmanager
from time import perf_counter

@contextmanager
def timeit(name):
    bef = perf_counter()
    yield
    print(name, "took", round(perf_counter() - bef, 4), "seconds")

with timeit("is_prime test suite"):
    assert(is_prime(2))
    assert(is_prime(3))
    assert(is_prime(5))
    assert(is_prime(7))
    assert(is_prime(11))
    assert(is_prime(13))
    assert(is_prime(17))
    assert(is_prime(23))
    assert(is_prime(29))
    assert(is_prime(31))
    assert(is_prime(37))
    assert(not is_prime(-1))
    assert(not is_prime(0))
    assert(not is_prime(4))
    assert(not is_prime(6))
    assert(not is_prime(9))
    assert(not is_prime(15))
    assert(not is_prime(25))

with timeit("prime_factors test suite"):
    assert(list(prime_factors(2)) == [2])
    assert(list(prime_factors(3)) == [3])
    assert(list(prime_factors(5)) == [5])
    assert(list(prime_factors(2 * 3 * 5 * 7)) == [2, 3, 5, 7])
    assert(list(prime_factors(2 * 2 * 3 * 3 * 5 * 5 * 7 * 7)) == [2, 2, 3, 3, 5, 5, 7, 7])

with timeit("all_factors test suite"):
    assert(all_factors(512) == {1, 2, 4, 8, 16, 32, 64, 128, 256, 512})
    assert(all_factors(2 * 3 * 5) == {1, 2, 3, 5, 2 * 3, 2 * 5, 3 * 5, 2 * 3 * 5})

with timeit("is_prime perf test"):
    assert(is_prime(2 ** 61 - 1))

with timeit("prime_factors perf test"):
    assert(list(prime_factors(2 ** 61 - 1)) == [2 ** 61 - 1])

