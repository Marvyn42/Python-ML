import sys

if len(sys.argv) != 2:
    sys.exit(print("Error: You must have 1 argument."))
elif sys.argv[1].isdigit() is False:
    sys.exit(print("Error: Only digits are accepted."))

if sys.argv[1] == 0:
    result = "Zero"
elif int(sys.argv[1]) % 2:
    result = "Odd"
else:
    result = "Even"
print("I'm %s." % result)
