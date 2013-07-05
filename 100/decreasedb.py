## aiming at select part of data from db
import sqlite3
con = sqlite3.connect("bd2re100")
cu = con.cursor()
cons = sqlite3.connect("bdre100")
cus = cons.cursor()
cus.execute('''create table if not exists doc(id integer, query text, name text, size text, version text, date text, download text, link text, package_name text, score real)''') 
a = [0, 'query', 'a', 'b', 'c', 'd', 'e', 'f','g', 0]
con.commit()
i = 0
f = cu.execute('select * from doc')
rows = f.fetchall()
for row in rows:
	if i < 100:
#	cus.execute('insert into doc valeus(?,?,?,?,?,?,?,?,?,?)', (row,))
		cus.execute('insert into doc values(?,?,?,?,?,?,?,?,?,?)',row)
		cons.commit()
	i = i + 1
