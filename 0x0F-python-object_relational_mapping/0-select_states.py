#!/usr/bin/python3
import MySQLdb
db = MySQLdb.connect(
        username = "root",
        password = "",
        database = "hbtn_0e_0_usa"
        )
cur = db.cursor()
cur.execute("SELECT * FROM states  WHERE name LIKE 'N%' ORDER BY id ASC")
rows = cur.fetchall()
for row in rows:
    print(row)

cur.close
db.close
