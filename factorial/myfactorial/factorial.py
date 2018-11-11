# "myfactorial" module


def factorial(num):
    """
    Returns the factorial value of the given number.
    A factorial is the product of an integer & all integers below it.

    :arg num: Integer value to calculate factorial of.

    :return: The value of the factorial, or -1 if a negative value is passed.

    """
    if num >= 0:
        if num == 0:
            return 1
        return num * factorial(num - 1)
    else:
        return -1
