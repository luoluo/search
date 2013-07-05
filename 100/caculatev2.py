#!usr/bin/python 
#-*- coding: utf-8 -*-
import operator
import math
import re
import sqlite3
def cc(score, pos):  # caculate score for current position
	return (pow(2, score) - 1)/(math.log((1+pos), 2)) 

conf = sqlite3.connect('maxdcg')
cons = sqlite3.connect('bdre100')
conw = sqlite3.connect('bdre100rep')
cf = conf.cursor()
cs = cons.cursor()
cw = conw.cursor()
cw.execute('''create table if not exists docr(id integer, query text, name text, score real, dcg real, ndcg real)''') 
a = [0, 'query', 'name', 0, 0, 0] 
fs = cons.execute('select * from doc')
rows = fs.fetchall()
for row in rows:
	iid = row[0] % 10 + 1
	ff = cf.execute('select * from dcg where query = ? and id = ?', (row[1], iid, ))
	mdcg = ff.fetchone()
	if mdcg == None:
		print row
	a[4] = mdcg[2]
	a[0] = row[0]	
	a[1] = row[1]
	a[2] = row[2]
	com = row[9]
	if a[0] % 10 == 0:
		a[3] = 0
	a[3] += cc(com, a[0] % 10 + 1)	
	a[5] = a[3] / a[4]
	cw.execute('insert into docr values(?,?,?,?,?,?)',  a)
	conw.commit()

#		c.execute('update doc set dcg = ? where id = ?', (int(dd), ee))
		#conn.commit()
