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
                SELECT cities.name FROM cities
                JOIN states ON cities.state_id = states.id
                WHERE states.name LIKE BINARY %s
                ORDER BY cities.id
                """,
        (sys.argv[4],),
    )

    query_rows = cur.fetchall()
    if query_rows is not None:
        print(", ".join([row[0] for row in query_rows]))

    cur.close()
    conn.close()
