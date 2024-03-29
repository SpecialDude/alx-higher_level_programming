#!/usr/bin/python3

"""
Even I does'nt know what this program does
Just another program that does a thing with a thing
"""


import sys


def main():
    """
    Program Entry point
    """

    file_size = 0

    status_codes = {
        '200': 0, '301': 0,
        '400': 0, '401': 0,
        '403': 0, '404': 0,
        '405': 0, '500': 0
    }

    i = 0
    try:
        while True:

            if sys.stdin.isatty():
                break

            line = sys.stdin.readline().rstrip("\n")

            metrics = line.split()

            size = int(metrics[-1])
            status = metrics[-2]

            status_codes[status] = status_codes[status] + 1
            file_size += size

            i += 1

            if i == 10:

                print("File size: {}".format(file_size))

                for key, value in status_codes.items():
                    if value == 0:
                        continue
                    print("{}: {:d}".format(key, value))

                i = 0
    except KeyboardInterrupt:
        print("File size: {}".format(file_size))

        for key, value in status_codes.items():
            if value == 0:
                continue
            print("{}: {:d}".format(key, value))

        raise


if __name__ == "__main__":
    main()
