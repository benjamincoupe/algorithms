"""

Fibonacci Sequence - Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.

"""


def Fibonacci(num):
    if num == 0:
        value = 0
        sequence = [value]
    elif num == 1:
        value = 1
        sequence = [0, value]
    else:
        value = Fibonacci(num-1)[0] + Fibonacci(num-2)[0]
        sequence = Fibonacci(num-1)[1]
        sequence += [value]
    return value, sequence


def main():
    for n in range(0, 20):
        print(Fibonacci(n)[1])


if __name__ == '__main__':
    main()




# Output should be 0, 1, 1, 2, 3, 5, 8, 13, 21