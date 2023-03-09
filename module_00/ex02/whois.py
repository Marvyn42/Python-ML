import sys


def whois(integer: int):
    if integer == 0:
        result = "Zero"
    elif int(integer) % 2:
        result = "Odd"
    else:
        result = "Even"
    print("I'm %s." % result)
    sys.exit(0)


if len(sys.argv) != 2:
    sys.exit(print("Error: You must have 1 argument."))
elif (sys.argv[1].isdigit() or
      (sys.argv[1][0] == "-" and sys.argv[1][1:].isdigit())):
    whois(sys.argv[1])
sys.exit(print("Error: Only digits are accepted."))
