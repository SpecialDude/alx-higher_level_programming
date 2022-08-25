#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    print(
        *list(filter(lambda x: not x.startswith('__'), dir(hidden_4))),
        sep="\n"
    )
