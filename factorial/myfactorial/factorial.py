# A factorial is the product of an integer & all integers below it.
import sys


def factorial(num):
    """
    Returns the factorial value of the given number.

    :arg num: Integer value to calculate factorial of.
    :return: The factorial of num

    """
    if num == 0:
        return 1
    return num * factorial(num - 1)


def div(num):
    """
    Divides 10 by num
    """
    return 10 / num


def main(num):
    print(factorial(num))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
