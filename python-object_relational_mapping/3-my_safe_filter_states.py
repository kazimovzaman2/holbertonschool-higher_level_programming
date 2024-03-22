#!/usr/bin/python3

"""
Filter states by user input
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

    cur.execute(
        """
                SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id
                """,
        (sys.argv[4],),
    )
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    cur.close()
    conn.close()
