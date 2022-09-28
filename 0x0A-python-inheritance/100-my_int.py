#!/usr/bin/python3

class MyInt(int):
    """MyInt is a rebel, it has its equality operations reversed"""

    def __eq__(self, __x: object):
        """Rebeled Equality Check

        Args:
            __x: int object

        Returns:
            bool
        """
        return not super().__eq__(__x)

    def __ne__(self, __x: object) -> bool:
        """Rebeled Inequality Check

        Args:
            __x: int object

        Returns:
            bool
        """
        return not super().__ne__(__x)
