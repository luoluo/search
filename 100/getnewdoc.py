import sqlite3

conf = sqlite3.connect("ddre100")
cons = sqlite3.connect("bdre100")
cone = sqlite3.connect("new100")
curf = conf.cursor()
curs = cons.cursor()
cure = cone.cursor()
cure.execute('''create table if not exists doc(id integer, query text, name text, size text, version text, date text, download text, link text, package_name text,  score real)''') 
a = [0, 'query', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 0]
f = curs.execute('select * from doc')
rows = f.fetchall()
for row in rows:
	result = curf.execute('select * from doc where query = ? and package_name = ?', (row[1], row[8]))
	newrows = result.fetchall()	
	if len(newrows) != 0:
		print"exist" + str(newrows)
	else:
		cure.execute('insert into doc values(?,?,?,?,?,?,?,?,?,?)', row);
		cone.commit()
#		print "not exist" + str(newrows)
		
