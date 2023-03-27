from sys import exit
import random


def generator(text: str, sep=" ", option=None):
    """Splits the text according to sep value and yield the substrings.
option precise if a action is performed to the substrings before it \
is yielded."""

    if not isinstance(text, str) or\
       (option is not None and option not in ["shuffle", "unique", "ordered"]):
        exit("ERROR")

    if (sep == ""):
        return text
    words_list = text.rsplit(sep)
    if (len(words_list) == 1):
        return text

    tmp = []
    if option is "shuffle":
        for _ in range(0, len(words_list)):
            word = random.choice(words_list)
            tmp.append(word)
            words_list.remove(word)
        words_list = tmp
    elif option is "unique":
        for word in words_list:
            if word not in tmp:
                tmp.append(word)
        words_list = tmp
    elif option is "ordered":
        tmp = sorted(words_list)
        words_list = tmp
    for word in words_list:
        if word != "":
            yield word
