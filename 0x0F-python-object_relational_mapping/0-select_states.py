#!/usr/bin/python3

""" This module lists all states in the database
hbtn_0e_0_usa
"""

import MySQLdb

db = MySQLdb.connect(host='localhost', port=3306, user='root', passwd='root',
        db='hbtn_0e_0_usa')
cur = db.cursor()

cur.execute('SELECT * FROM states ORDER BY states.id');

rows = cur.fetchall()

for row in rows:
    print(row)
