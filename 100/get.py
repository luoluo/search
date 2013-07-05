import urllib2, urllib
import simplejson
import sqlite3
url = 'http://10.2.8.166/label/api/task/result?id=17&skip=0&limit=187'
f = urllib2.urlopen(url)
html = f.read()
jhtml = simplejson.loads(html)
con = sqlite3.connect("final")
cu = con.cursor()
st = cu.execute('select * from doc')
rows = st.fetchall()
row_id = 0
for row in rows:
	com = jhtml['items'][row_id]['label']['choose']
	query = jhtml['items'][row_id]['content']['query']
	pkg_name = jhtml['items'][row_id]['content']['package_name']
	score = 0
	if com == 'Perfect':
		score = 5
	if com == 'Excellent':
		score = 4
	if com == 'Good':
		score = 3
	if com == 'Fair':
		score = 2
	row_id += 1
#	print score
	cu.execute('update doc set score = ? where query = ? and package_name = ?', (score, query, pkg_name))
	con.commit()
