#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    c = len(sys.argv) - 1
    if c != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if sys.argv[2] not in ["+", "-", "*", "/"]:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    operation = sys.argv[2]
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    
    if operation == "+":
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif operation == "-":
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif operation == "*":
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif operation == "/":
        print("{} / {} = {}".format(a, b, div(a, b)))
    sys.exit(0)
