"""

Prime Factorization - Have the user enter a number and find all Prime Factors (if there are any) and display them.

"""

# This finds if any given number is prime
def isprime(num):
    factors = []
    for n in range(1, num):
        left = num % n
        if left == 0:
            if (n != num) and (n != 1):
                factors += [n]
    if len(factors) > 0:
        return False
    return True

def list_prime(num):
    # This finds all prime numbers between 2 and number: Not what I want
    # It should find the remainder of
    primes = []
    final = []
    for n in range(2, num):
        if isprime(n):
            primes.append(n)
    for n in primes:
        if num % n == 0:
            final.append(n)
    return final


if __name__ == "__main__":

    for n in range(2, 50):
        print(n, list_prime(n))

