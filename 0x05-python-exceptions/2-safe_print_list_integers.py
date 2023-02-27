#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Safely print any list

    Args:
        my_list: list
        x: number of elements to print

    Returns:
        int
    """

    c = 0

    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            c += 1
        except IndexError:
            raise
        except Exception:
            pass

    print()

    return (c)
