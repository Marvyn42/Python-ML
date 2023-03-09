import sys
import string


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Error: the program is waiting for 2 arguments only.")
    if type(sys.argv[1]) is not str or sys.argv[2].isdigit() is False:
        sys.exit("Error:\nUsage: python filterwords.py [string] [int]")
    new_str = sys.argv[1].translate(str.maketrans('', '', string.punctuation))
    list = new_str.split()
    new_list = []
    for str in list:
        if len(str) > int(sys.argv[2]):
            new_list.insert(len(new_list), str)
    print(new_list)
    sys.exit(0)
