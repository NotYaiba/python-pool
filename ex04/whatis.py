import sys

def is_even_or_odd():
    # Check number of arguments
    if len(sys.argv) != 2:
        print("AssertionError: more than one argument is provided" if len(sys.argv) > 2 else "AssertionError: no argument is provided")
        return 
    arg = sys.argv[1]
    
    try:
        number = int(arg)
    except:
        print("AssertionError: argument is not an integer")
        return

    # Print result
    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

if __name__ == "__main__":
    is_even_or_odd()