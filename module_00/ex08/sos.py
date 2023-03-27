import sys

dict_morse = {'A': '.-', 'B': '-...',
              'C': '-.-.', 'D': '-..', 'E': '.',
              'F': '..-.', 'G': '--.', 'H': '....',
              'I': '..', 'J': '.---', 'K': '-.-',
              'L': '.-..', 'M': '--', 'N': '-.',
              'O': '---', 'P': '.--.', 'Q': '--.-',
              'R': '.-.', 'S': '...', 'T': '-',
              'U': '..-', 'V': '...-', 'W': '.--',
              'X': '-..-', 'Y': '-.--', 'Z': '--..',
              '1': '.----', '2': '..---', '3': '...--',
              '4': '....-', '5': '.....', '6': '-....',
              '7': '--...', '8': '---..', '9': '----.',
              '0': '-----', ' ': '/'}


if __name__ == "__main__":
    if (len(sys.argv) < 2):
        sys.exit(0)

    for str in sys.argv[1:]:
        for c in str:
            if c.isalnum() is False and c != " ":
                sys.exit("ERROR")
    sos_mess = " ".join(sys.argv[1:])
    morse_mess = ""
    for c in sos_mess:
        morse_mess += (dict_morse[c.upper()] + " ")
    print(morse_mess[:-1])
