def NULL_not_found(object) -> int:
    if object is None:
        print("Nothing: None <class 'NoneType'>")
    elif type(object) == float and object != object:  # NaN is not equal to itself
        print("Cheese: nan <class 'float'>")
    elif type(object) == int and object == 0:
        print("Zero: 0 <class 'int'>")
    elif type(object) == str and object == '':
        print("Empty:  <class 'str'>")
    elif type(object) == bool and object is False:
        print("Fake: False <class 'bool'>")
    else:
        print("Type not Found")
        return 1
    return 0