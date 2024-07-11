#!/usr/bin/python3
"""Takes in arguments and displays all values in the state
where name matches argument. Improved from filter 2 to avoid SQLinjections"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cr = db.cursor()
    cr.execute("SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC",
               (argv[4],))
    rows = cr.fetchall()
    for row in rows:
        print(row)
    cr.close()
    db.close()
