#!/usr/bin/python3
""" script that list all cities
in a database
"""
import MySQLdb
import sys
if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306
            )
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM\
            cities JOIN states ON cities.states_id = states.id \
            WHERE states.name LIKE BINARY %(name)s \
            ORDER BY cities ASC",{'name': sys.argv[4]})
    rows = cur.fetchall()
    if rows is not None:
        print(", ".join([row[1] for row in rows)
    cur.close()
    db.close()
