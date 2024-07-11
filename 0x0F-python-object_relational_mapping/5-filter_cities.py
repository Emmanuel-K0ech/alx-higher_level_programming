#!/usr/bin/python3
"""Takes in the name of a state as an argument and lists
all cities of that state"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cr = db.cursor()
    cr.execute("SELECT cities.name FROM cities \
    JOIN states ON cities.state_id = states.id WHERE states.name LIKE %s \
    ORDER BY cities.id", (argv[4],))
    rows = cr.fetchall()
    print(", ".join(city[0] for city in rows))
    cr.close()
    db.close()
