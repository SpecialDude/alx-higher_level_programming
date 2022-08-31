#!/usr/bin/python3
def roman_to_int(roman_string):
    """Converts a Roman numeral to an integer.

    Args:
        roman_string: String

    Returns:
        Integer
    """
    roman_literals = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    equi_int = [1, 5, 10, 50, 100, 500, 1000]

    if not roman_string:
        return 0
    if len(roman_string) == 1:
        return equi_int[roman_literals.index(roman_string)]

    first = roman_string[0]
    next = roman_string[1]

    fvalue = equi_int[roman_literals.index(first)]
    nvalue = equi_int[roman_literals.index(next)]

    return ((-1 if fvalue < nvalue else 1) * fvalue) + \
        roman_to_int(roman_string[1:])
