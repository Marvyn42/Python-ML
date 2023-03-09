import sys


def apply_operations(integer_1, interger_2):
    """
    Print the operation's result of two integers:
    - Sum;
    - Difference;
    - Product;
    - Quotient;
    - Remainder.
    """

    try:
        print(f'Sum:\t\t{integer_1 + interger_2}')
        print(f'Difference:\t{integer_1 - interger_2}')
        print(f'Product:\t{integer_1 * interger_2}')
        print(f'Quotient:\t{integer_1 / interger_2}')
        print(f'Remainder:\t{integer_1 % interger_2}')
    except ZeroDivisionError:
        print("Quotient:\tERROR (division by zero)")
        print("Remainder:\tERROR (modulo by zero)")


if __name__ == "__main__":
    if len(sys.argv) != 3 or not sys.argv[1].isdigit() \
       or not sys.argv[2].isdigit():
        print("Usage: python operations.py <number1> <number2>") if \
            len(sys.argv) == 1 else print("Error: Two integers only.")
        sys.exit(0)
    apply_operations(int(sys.argv[1]), int(sys.argv[2]))
    sys.exit(0)
