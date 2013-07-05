import sqlite3
conf = sqlite3.connect("final")
cons = sqlite3.connect("bdre100")
curf = conf.cursor()
curs = cons.cursor()
f = cons.execute("select * from doc")
rows = f.fetchall()
for row in rows:
	query = row[1]
	pkg_name = row[8]
	ff = curf.execute("select * from doc where query = ? and package_name = ?", (query, pkg_name))
	findone = ff.fetchone()
	if findone == None:
		print  row
	else:
		score = findone[9]
		curs.execute("update doc set score = ? where query = ? and package_name = ?", (score, query, pkg_name))
		cons.commit()
