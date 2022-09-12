#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """List Division

    Args:
        my_list_1: list
        my_list_1: list
        list_length: int

    Returns:
        list
    """

    result = [0] * list_length

    for i in range(list_length):
        try:
            res = my_list_1[i] / my_list_2[i]
            result[i] = res
        except ZeroDivisionError:
            print("division by 0")

        except TypeError:
            print("wrong type")

        except IndexError:
            print("out of range")
        finally:
            pass

    return result
