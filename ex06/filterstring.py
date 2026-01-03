import sys
from ft_filter import ft_filter


def filterstring():
    """
    Filter and print words longer than a given length.

    Expects two CLI args:
    - sys.argv[1]: space-separated words
    - sys.argv[2]: integer min length

    Uses ft_filter to keep words with len(word) > min
    length and prints the result.
    On invalid args, prints: 'AssertionError: the arguments are bad.'

    Example:
        python filterstring.py "hello world from python" 4
        -> ['hello', 'world', 'python']
    """
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad.")
        number = int(sys.argv[2])
        wlist = sys.argv[1].split(' ')
        new = ft_filter(lambda x: len(x) > number, wlist)
        print(new)
    except Exception:
        print('AssertionError: the arguments are bad.')


def main():
    filterstring()


if (__name__ == "__main__"):
    main()
