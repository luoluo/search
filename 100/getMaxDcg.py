import sqlite3
import re
import math
def cc(score, pos):  # caculate score for current position
	return (pow(2, score) - 1)/(math.log((1+pos), 2)) 
conf = sqlite3.connect("final")
#cons = sqlite3.connect("")
cone = sqlite3.connect("maxdcg2")
curf = conf.cursor()
#curs = cons.cursor()
cure = cone.cursor()
cone.execute("create table if not exists dcg(query text, id integer, score real)")
a = ["query", 0, 0]
conq = sqlite3.connect("queryTable-")
curq = conq.cursor()
f = conq.execute("select * from query")
querySets = f.fetchall()
i = 0
for querySet in querySets:
	if i < 10:
		query = querySet[1]
		print "\n--" + query + "--\n"
		fs = curf.execute('select * from doc where query=:qr', {"qr":query})
		rows = fs.fetchall()
#	for row in rows:
#		print row[9]
		rows.sort(key=lambda x: (x[9], x[0]), reverse=True)
#	print "---"
#	for row in rows:
#		print row[9]
#	break
		a[2] = 0
		a[1] = 1
		for row in rows:
			if a[1] < 11:
				a[0] = row[1]
				score = row[9]
		#		print score	
				a[2] += cc(score, a[1])
				cure.execute('insert into dcg values(?,?,?)', a)
				cone.commit()
				a[1] += 1
	i += 1
