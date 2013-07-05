import sqlite3
dcon = sqlite3.connect("ddre100")
bcon = sqlite3.connect("new100")
dbcon = sqlite3.connect("final")
dcur = dcon.cursor()
bcur = bcon.cursor()
dbcur = dbcon.cursor()
dbcur.execute('''create table if not exists doc(id integer, query text, name text, size text, version text, date text, download text, link text, package_name text, score real)''') 

df = dcur.execute("select * from doc")
bf = bcur.execute("select * from doc")
drows = df.fetchall()
brows = bf.fetchall()
for drow in drows:
	dbcur.execute("insert into doc values(?,?,?,?,?,?,?,?,?,?)", drow)
for brow in brows:
	dbcur.execute("insert into doc values(?,?,?,?,?,?,?,?,?,?)", brow)
dbcon.commit()
		
