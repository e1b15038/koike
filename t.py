import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    port = 8889,
    user = 'root',
    password = 'root',
    database = 'diagram',
)

connected=conn.is_connected()
print(connected)
if(not connected):
    conn.ping(True)

cur = conn.cursor()

AA='芦屋発'
cur.execute('SELECT * FROM type06 ORDER BY AA LIMIT 1')

#table = cur.fetchall()
#print(table)

print(cur.statement)
print(cur.fetchone())
