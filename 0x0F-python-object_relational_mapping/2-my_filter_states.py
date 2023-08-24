#!/usr/bin/python3
"""
Takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.
Usage: ./2-my_filter_states.py <mysql username> \
                                <mysql password> \
                                <database name> \
                                <state name searched>
"""
import sys
import MySQLsb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], port=3306, host="localhost",
                         passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY id ASC".format(sys.argv[4]))
    states = c.fetchall()
    for state in states:
        if state[1] == sys.argv[4]:
            print(state)
    c.close()
    db.close()
