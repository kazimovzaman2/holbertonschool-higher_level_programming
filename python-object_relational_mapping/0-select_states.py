#!/usr/bin/python3

"""
Get all states from the database hbtn_0e_0_usa
"""

import sys
import MySQLdb


if __name__ == "__main__":
    conn = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )
    cur = conn.cursor()

    cur.execute("SELECT * FROM states")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    cur.close()
    conn.close()
