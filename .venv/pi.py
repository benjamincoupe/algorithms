"""

Find PI to the Nth Digit - Enter a number and have the program generate PI up to that many decimal
places. Keep a limit to how far the program will go.

"""
import numpy as np


def remove(string, i):
    a = string[: i]
    b = string[i + 1:]
    return a + b


def nth_digit(digit):
    if digit == 0:
        value = (str(pi))[:digit+1]
    elif (digit > 0) and (digit < 16):
        value = (str(pi))[:digit+2]
    elif digit < 0 or (digit >= 16):
        digit = int(input("Enter a number between 0 and 15 here: "))
        value = (str(pi))[:digit+1]
    return value










# Driver Code
if __name__ == '__main__':
    pi = np.pi

    print(nth_digit(17))






# Output should be {0:3, 1:1, 2:4, 3:1, 4:5}

# I am only returning the nth digit, not pi to that digit