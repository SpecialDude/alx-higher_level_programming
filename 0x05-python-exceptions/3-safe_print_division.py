#!/usr/bin/python3

def safe_print_division(a, b):
    """Safe division

    Args:
        a: num
        b: num

    Returns:
        int
    """

    result = None

    try:
        result = a / b
    except ZeroDivisionError:
        pass
    finally:
        print("Inside result: {}".format(result))

    return result
