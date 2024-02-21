"""

Next Prime Number - Have the program find prime numbers until the user chooses to stop asking for the next one.

"""

# This finds if any given number is prime
def isprime(num):
    factors = []
    for n in range(1, num):
        left = num % n
        if left == 0:
            if (n != num) and (n != 1):
                factors += [n]
    if len(factors) > 0 or (num == 0) or (num==1):
        return False
    return True

def next_prime(num):
    prime = isprime(num)
    while not prime:
        num+=1
        prime = isprime(num)
    return num

if __name__ == '__main__':
    num = int(input("Enter the number here: "))
    first_prime = next_prime(num)
    print(first_prime)
    done = False
    while not done:
        decision = str(input("Do you want the next prime number? (y or n): "))
        if decision == 'y':
            num +=1
            new_prime = next_prime(num)
            while new_prime == first_prime:
                num+=1
                new_prime = next_prime(num)
            first_prime = new_prime
            print(next_prime(num))
        else:
            done = True

# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199
