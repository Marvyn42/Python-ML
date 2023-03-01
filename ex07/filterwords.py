import sys


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Error: the program is waiting for 2 arguments only.")
    if sys.argv[1].isalpha() is False or sys.argv[2].isdigit() is False:
        sys.exit("Error:\nUsage: python filterwords.py [string] [int]")
    sys.exit(0)
