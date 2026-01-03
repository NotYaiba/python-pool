import sys
MORSE_CODE_DICT = {
    'A': '.-',    'B': '-...',  'C': '-.-.',
    'D': '-..',   'E': '.',     'F': '..-.',
    'G': '--.',   'H': '....',  'I': '..',
    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',
    'S': '...',   'T': '-',     'U': '..-',
    'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..',

    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', ' ': '/'
}


def sos():
    """
    Convert a single command-line argument to Morse code and print the result.

    This function:
    - Validates that exactly one argument is provided via sys.argv.
    - Ensures all characters in the argument exist in MORSE_CODE_DICT.
    - Converts the argument to uppercase and maps each character to Morse code.
    - Prints the Morse sequence with spaces between encoded characters.

    If validation fails, prints
    "AssertionError: the arguments are bad" and returns.

    Returns:
        None
    """
    sostxt = ''
    if (len(sys.argv) != 2):
        print('AssertionError: the arguments are bad')
        return
    arg = sys.argv[1].upper()
    if (not all(char in MORSE_CODE_DICT for char in arg)):
        print("AssertionError: the arguments are bad")
        return
    index = 0
    for char in arg:
        if (len(arg) - 1 == index):
            sostxt += MORSE_CODE_DICT[char]
        else:
            sostxt += MORSE_CODE_DICT[char] + ' '
        index += 1
    print(sostxt)


def main():
    sos()


if __name__ == '__main__':
    main()
