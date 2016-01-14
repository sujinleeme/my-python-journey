'''
Counting Organizations
This application will read the mailbox data (mbox.txt) count up the number
email messages per organization (i.e. domain name of the email address)
using a database with the following schema to maintain the counts.
'''


import sqlite3, re

conn = sqlite3.connect('email-db.sqlite')
curs = conn.cursor()

curs.execute('DROP TABLE IF EXISTS Counts')
curs.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

fh = open('mbox.txt')
for line in fh:
    if not line.startswith('From: ') : continue
    email = "".join(re.findall('(?<=@).+', line))
    print (email)
    
    curs.execute('SELECT count FROM Counts WHERE org=?', (email, ))
    row = (curs.fetchone())
    if row is None:
        curs.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (email,))
    else:
        curs.execute('UPDATE Counts SET count=count+1 WHERE org=?', (email,))
    conn.commit()

curs.close()
