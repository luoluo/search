#!/usr/bin/python
#encoding:utf-8
import time
import urllib2
import re
import pymongo
import sqlite3
import HTMLParser

#db = pymongo.Connection('localhost', 27017)
#client = pymongo.MongoClient("localhost", 27017)
#db = client.test
conn = sqlite3.connect('re1')
#conn.text_factory = str
#sqlite3.ProgrammingError: You must not use 8-bit bytestrings unless you use a text_factory that can interpret 8-bit bytestrings (like text_factory = str). It is highly recommended that you instead just switch your application to Unicode strings.
c = conn.cursor()
#c.execute('''create table stocks (name text, size text, version text, date text, download text, link text)''') 
#c.execute("""insert into stocks values('yyy', '123', '1.1.1', '123415', '4444444', 'httpsadf')""")
#conn.commit()
#rec = c.execute('''select * from stocks''')
#print c.fetchall()

c.execute('''create table if not exists doc(query text, name text, size text, version text, date text, download text, link text, score real)''') 
#c.execute("""insert into doc values('yyy', '123', '1.1.1', '123415', '4444444', 'httpsadf', 0)""")
a = ['query', 'a', 'b', 'c', 'd', 'e', 'f', 0]
#c.execute('insert into doc values(?,?,?,?,?,?,?)', (a[0], a[1], a[2], a[3], a[4], a[5], 6))
conn.commit()

#rec = c.execute('''select * from doc''')
#print c.fetchall()

url2 = 'http://m.baidu.com/s?st=10a001&tn=webmkt&pre=web_am_index&word='

#a = list(7)
queriesBook = open("result2")
while True :
	i = queriesBook.readline();
	if len(i) == 0:
		break
	
	temp = re.match(r'.*=(.*),.*', i)
	query = temp.group(1)
	a[0] = query.decode("utf8")
	print "\n\n" + query + "\n"
#	print query 

	url5 = url2 + "" + query
	f = urllib2.urlopen(url5) #the web page infomation is in html
	html = f.read()
	time.sleep(1)   
	#html = unicode(html, "gb2312").encode("utf8")
	
	####   To match ####
	name = re.compile(r'h4>(.*)')
	size = re.compile(r'.*?>(.*MB).*')
	version = re.compile(r'.*(软件版本.*)')
	date = re.compile(r'.*(更新日.*)')
	download = re.compile(r'.*(下载次数.*)')
	link = re.compile(r'img.*src="(http:[\w\W]*).*" alt')
#c.execute('''create table if not exists doc(name text, size text, version text, date text, download text, link text, score real)''') 
			#<img src="http://hiphotos.baidu.com/wisegame/pic/item/fd2f070828381f309e45f8e6a8014c086e06f025.jpg" id="app-logo" alt="QQ"">
	
	lines = html.split('<')
	for line in lines:
	#	print line
		
		match = name.match(line)  
		if match:
			a[1] = match.group(1).decode("utf8")
#			print 'name = ' + a[0]
#			a[0] = unicode(match.group(1))
	
		match = size.match(line)   
		if match:
			a[2] = match.group(1).decode("utf8")
#			print 'size = ' + a[1]

		match = version.match(line)
		if match:
			a[3] = match.group(1).decode("utf8")
#			print 'version = ' + a[2]
#			a[2] = unicode(match.group(1))
	
		match = date.match(line)   
		if match:
			a[4] = match.group(1).decode("utf8")
#			print 'date = ' + a[3]
#			a[3] = unicode(match.group(1))
	
		match = download.match(line)   
		if match:
			a[5] = match.group(1).decode("utf8")
#			print 'download = ' + a[4]
#			c.execute('insert into doc values(?,?,?,?,?,?,?)', (a[0], a[1], a[2], a[3], a[4], a[5], 0))
			c.execute('insert into doc values(?,?,?,?,?,?,?,?)', a)
			conn.commit()
#			a[4] = unicode(match.group(1))

	
		match = link.match(line)
		if match:
			a[6] = match.group(1).decode("utf8")
#			print 'link = ' + a[5]
#			c.execute('insert into doc values("%s,%s,%s,%s,%s,%f")', a)
			
#c.execute("""insert into doc values('yyy', '123', '1.1.1', '123415', '4444444', 'httpsadf', 0)""")
		
#	rec = c.execute('''select * from doc''')
#	t = ('qq',)
#	rec = c.execute('select * from doc where name = ?', t)

#	rec = c.execute('select * from doc')
#	r = c.fetchone()
#	print r[2]	

#	r.keys() 	#why not work?????
#	for i in r.keys():
#		print r[i] + "\n"

#	for row in c.execute('select * from doc order by name'):
#		print row
	f.close()
queriesBook.close()
