def nums(*args):
    if not args:
        return "Data cannot be empty"

    for num in args:
        if not isinstance(num, (int, float)): # checks wether the input(num)in args are number or any other type.
            return "Enter correct inputs"

    largest = float('-inf')
    smallest = float('inf')

    for num in args:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num

    return largest, smallest

    