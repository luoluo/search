from django.http import HttpResponse
import re
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context
from django import forms
import sqlite3
import sys

def hello(request):
	conn = sqlite3.connect("re2")
	c = conn.cursor()
	html = ""
	if 'q' in request.GET:
		ss = request.GET['q']

		dd = re.match(r'(\d)%.*%.*',ss)
		if dd:
			dd = dd.group(1)
			
		rr = re.match(r'\d%(\D*)%.*', ss)
		if rr:
			rr = rr.group(1)

		ee = re.match(r'\d%.*%(\d+)', ss)
		if ee:
			ee = ee.group(1)
		
		c.execute('update doc set score = ? where id = ?', (int(dd), ee))
		conn.commit()

		iee = int(ee)
		iee = iee + 1 

##### why both work?? ####
#		r = c.execute('select * from doc where id = "15"')
#		r = c.execute('select * from doc where id = 15')
		r = c.execute("select * from doc where id=:Id", {"Id":iee})
	else:
		r = c.execute('select * from doc where id = 0')
		html = ""
	rows = r.fetchone()
	if rows == None:
		html = "We've done, thank you for voting!!!"
		return HttpResponse(html)
	t = get_template('score.html')
	html = html +(t.render(Context({'iid':rows[0],
								  'qname': rows[1],
								  'row1': rows[2] ,
								  'row2': rows[3] ,
								  'row3': rows[4] ,
								  'row4': rows[5] ,
								  'row5': rows[6] ,
								  'row6': rows[8] ,
								  'row7': rows[7]}
			)))
	return HttpResponse(html)
def caculate(request):
	conn = sqlite3.connect("re2")
	c = conn.cursor()
	
