"""
When setup.py calls us, we should set up the database for this year's
ARRL Field Day contest.
"""

import sqlite3
import datetime

# Set the database name based on this year.
dbname=("agridieslog-"+str(datetime.date.today().year)+".db")


def dbsetup():
    conn = sqlite3.connect(dbname)
    c = conn.cursor()

    c.execute('''CREATE TABLE LOGS
             ([generate_id] INTEGER PRIMARY KEY,[band] text, [mode] text,
             [ocall] text, [ocat] text, [osec] text, [tcall] text, [tcat] text,
             [tsec] text, [datetime] text)''')

'''
LOGS - table rows:
    band - mode - ocall - ocat - osec - tcall - tcat - tsec - datetime
'''

def logwrite():
    conn = sqlite3.connect(dbname)
    c = conn.cursor()

    c.execute("INSERT INTO LOGS VALUES (band, mode, ocall, ocat, osec, tcall, tcat, tsec, datetime)")
