#!/usr/bin/python3

"""This module lists all states from a  database"""


import sys
import MySQLdb


def main():
    """
        The main program
        Readsall rows from a database table
    """

    args = sys.argv[1:]

    if len(args) == 3:
        username, password, dbname = args
    else:
        sys.exit()

    db = MySQLdb.connect(
        host='localhost',
        user=username,
        passwd=password,
        db=dbname,
        port=3306
    )

    cur = db.cursor()

    cur.execute("SELECT id, name FROM states WHERE name LIKE 'N%' ORDERBY id")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == "__main__":
    main()
