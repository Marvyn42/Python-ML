import sys
import string


def text_analyser(text=""):
    """
    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text.
    """
    if text == "":
        text = input("What is the text to analyze ?\n")
    if type(text) != str or text.isdigit():
        return (print("Error: Argument is not a string."))
    upper = 0
    lower = 0
    punct = 0

    for c in text:
        if c in string.ascii_uppercase:
            upper += 1
        elif c in string.ascii_lowercase:
            lower += 1
        elif c in string.punctuation:
            punct += 1
    print(f'The text contains {len(text)} character(s):',
          f'- {upper} upper letter(s)', f'- {lower} lower letter(s)',
          f'- {punct} punctuation mark(s)', f'- {text.count(" ")} space(s)',
          sep='\n')


if __name__ == "__main__":
    if len(sys.argv) > 2:
        sys.exit(print("Error: Too many arguments"))
    text_analyser("") if len(sys.argv) == 1 else text_analyser(sys.argv[1])
