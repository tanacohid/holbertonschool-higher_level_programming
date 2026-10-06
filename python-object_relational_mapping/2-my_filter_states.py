#!/usr/bin/python3

"""Script qui liste toutes les villes de la base de données."""
import MySQLdb
import sys

if __name__ == "__main__":
    sql_user_name = sys.argv[1]
    sql_password = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )

    cur = db.cursor()
    query = ("SELECT * FROM states WHERE name LIKE BINARY '{}' "
    "ORDER BY id ASC").format(sys.argv[4])
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
