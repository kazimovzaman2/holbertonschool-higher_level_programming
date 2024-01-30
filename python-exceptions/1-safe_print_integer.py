#!/usr/bin/python3
def safe_print_integer(value):
    flag = True
    try:
        print("{:d}".format(value))
        flag = True
    except ValueError:
        flag = False
    finally:
        return flag
