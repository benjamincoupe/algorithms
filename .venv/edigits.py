"""

Find e to the Nth Digit - Just like the previous problem, but with e instead of PI. Enter a number and have the program
generate e up to that many decimal places. Keep a limit to how far the program will go.

"""

import numpy as np


def find_digits(num):
    if num < 0 or num > 15:
        print("Enter a number between 0 and 15")
    elif num == 0:
        value = estr[0]
    else:
        value = estr[:num+2]
    return value

if __name__ == '__main__':
    estr = str(np.e)

    print(find_digits(int(input("Enter an integer between 0 and 15: "))))