#!/usr/bin/python3
def print_last_digit(number):
    digit = int(str(number)[-1:])
    print("{}".format(digit), end="")
    return digit
