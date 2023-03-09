import sys

if len(sys.argv) > 1:
    output = " ".join(sys.argv[1:])
    print(output[::-1].swapcase())
