"""

Binary to Decimal and Back Converter - Develop a converter to convert a decimal number to binary or a binary number to
its decimal equivalent.

"""

import math



def converter(num, direction):
    if direction == 'binary':
        binary_string = ''
        x = math.floor(math.log(num, 2))
        y = 2**x
        binary_string += '1'
        difference = num - y
        for i in reversed(range(0, x)):
            if 2**i > difference:
                binary_string += '0'
            elif 2**i <= difference:
                binary_string += '1'
                y = 2**i
                difference = difference - y
        return binary_string

    elif direction == 'decimal':
        dec_float = 0
        for n in enumerate(reversed(num)):
            x = n[0]
            include = n[1]
            if include == '1':
                y = 2**(x)
                dec_float += y
        return dec_float


if __name__ == '__main__':
    for i in range(1, 50):
        print(i, converter(i, 'binary'))
    print("")
    print(converter("1010010", 'decimal'))
