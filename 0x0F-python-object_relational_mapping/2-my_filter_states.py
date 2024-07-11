#!/usr/bin/python3
"""Script that takes an argument and displays all values in the states
table where name matches argument"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cr = db.cursor()
    cr.execute("SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY \
    id ASC".format(argv[4]))
    rows = cr.fetchall()
    for row in rows:
        if row[1] == argv[4]:
            print(row)
    cr.close()
    db.close()
