import psycopg2 as pg2
#Creating connection to DB
# conn = pg2.connect(database="dvdrental", user="postgres", password="postgres", host="localhost", port="5432")
conn = pg2.connect(database="dvdrental", user="postgres", password="password")
#Creating cursor - Cursor is used to iterate through returned data from query
cur = conn.cursor()
#executing the query
cur.execute("select * from payments")
#fetching the all the data from above query
data = cur.fetchall()
#fetching the 10 the data from above query
data = cur.fetchmany(10)
#fetching the 1 the data from above query
data = cur.fetchone(10)
#Close the connection
conn.close()
