import sqlite3

conn = sqlite3.connect('afternoon.db')
print("Opened database successfully")

conn.execute("INSERT INTO EMPLOYEES VALUES (1,'FAITH KARIMI',34,340000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (2,'JOHN KARIMI',50,380000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (3,'NICOLE MEDZA',21,490000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (4,'DUDLEY GEORGE',37,500000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (5,'DANIEL IMANI',25,620000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (6,'CLARKSON DAVID',27,990000.00)")

conn.commit()
print("Employees inserted successfully")
conn.close()