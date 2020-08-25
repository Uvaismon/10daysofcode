global _primes
global _prime_table
_primes = {2:2}
_prime_table = {0: 0, 1: 0}

def is_prime(n):
    global _primes
    if n < 2:
        return False
    for i in _primes:
        if i > n ** 0.5:
            break
        if n % i == 0:
            return False
    _primes[n] = n
    return True

def number_of_primes(n):
    global _prime_table
    number = 0
    for i in range(2,n + 1):
        if is_prime(i):
                number += 1
        _prime_table[i] = number

g = int(input())
test_cases = []
for _ in range(g):
    test_cases.append(int(input()))
core_case = max(test_cases)
number_of_primes(core_case)

for i in test_cases:
    if _prime_table[i] % 2 == 0:
        print('Bob')
    else:
        print('Alice')

