#!/usr/bin/python3
"""script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa"""

import MySQLdb
from sys import argv
if __name__ == "__main__":
    sqldb = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                                                      passwd=argv[2], db=argv[3], charset="utf8")
    current = sqldb.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    loop = current.fetchall()
    for i in loop:
        if i[1][0] == 'N':
            print(i)
            current.close()
            sqldb.close()
