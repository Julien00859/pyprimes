from itertools import combinations
from functools import partial, reduce
from operator import mul

mult = partial(reduce, mul)

def primes_candidate(candidate=0):
    if candidate < 2:
        candidate = 2
        yield candidate

    if candidate == 2:
        candidate = 3
        yield candidate

    if candidate < 5:
        candidate = 5
        yield candidate

    mod6 = candidate % 6
    if mod6 == 1:
        mod = 4
    elif mod6 == 5:
        mod = 2
    else:
        raise ValueError("%d is not a valid candidate" % candidate)

    while True:
        candidate += mod
        mod = 4 - mod
        yield candidate


def isqrt(n):
    from math import sqrt
    return int(sqrt(n))


def is_prime(n):
    if n < 2:
        return False
    if n < 4:
        return True

    isqrt_n = isqrt(n)
    for candidate in primes_candidate():
        if n % candidate == 0:
            return False
        if candidate >= isqrt_n:
            return True


def prime_factors(n):
    for candidate in primes_candidate():
        while n % candidate == 0:
            yield candidate
            n //= candidate
        if n == 1:
            break

def all_factors(n):
    factors = list(prime_factors(n))
    pairs = set([1])
    for i in range(1, len(factors) + 1):
        for comb in combinations(factors, i):
            pairs.add(mult(comb))
    return pairs


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

assert(list(prime_factors(2)) == [2])
assert(list(prime_factors(3)) == [3])
assert(list(prime_factors(4)) == [2, 2])
assert(list(prime_factors(5)) == [5])
assert(list(prime_factors(6)) == [2, 3])
assert(list(prime_factors(2 * 3 * 3 * 5)) == [2, 3, 3, 5])

assert(all_factors(512) == {1, 2, 4, 8, 16, 32, 64, 128, 256, 512})
assert(all_factors(2 * 3 * 5) == {1, 2, 3, 5, 2 * 3, 2 * 5, 3 * 5, 2 * 3 * 5})
