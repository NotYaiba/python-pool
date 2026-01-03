import sys


def building(arg):
    """Print a summary
    of character
    types in a given string
    (upper, lower, digits, spaces, punctuation)."""
    sums = 0
    upper = 0
    lower = 0
    spaces = 0
    digits = 0
    punctuation = 0
    for char in arg:
        if (char.isspace()):
            spaces += 1
        elif (char.islower()):
            lower += 1
        elif (char.isupper()):
            upper += 1
        elif (char.isdigit()):
            digits += 1
        else:
            punctuation += 1
        sums += 1
    print(f'The text contains {sums} characters:')
    print(f'{upper} upper letters')
    print(f'{lower} lower letters')
    print(f'{punctuation} punctuation marks')
    print(f'{spaces} spaces')
    print(f'{digits} digits')


def main():
    try:
        if (len(sys.argv) == 1):
            arg = input("What is the text to count?\n")
        elif len(sys.argv) > 2:
            raise AssertionError("More than one argument is provided")
        else:
            arg = sys.argv[1]
        building(arg)
    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    main()
