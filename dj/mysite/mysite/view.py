from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
import datetime
import sqlite3
import sys

def hello(request):
	conn = sqlite3.connect("re1.db")
	c = conn.cursor()
	r = c.execute('select * from doc')
	rows = r.fetchone()
	html = (
		"<html> <body> " + 
		"quriy name ==  " + rows[0]+ "<br>"	+ 
		"<table border=" + "1>"+
		"<tr>               "+
		"<td>"+rows[1]+"</td>"+
		"<td>"+rows[2]+"</td>"+
		"</tr>                 "+
		"<tr>                  "+
		"<td>"+rows[3]+"</td>"+
		"<td>"+rows[4]+"</td>"+
		"</tr>                 "+
		"<tr>                  "+
		"<td>"+rows[5]+"</td>"+
		"<td>"+rows[6]+"</td>"+
		"</tr>                 "+
		"</table>              "+
#		"<img src=" + rows[6] + " />"
		"<form>" +
		"<input type="+"\"radio\""+ "name="+"\"sex\""+" value="+"\"male\""+" /> Perfect"+
		"<br /> " + 
		"<input type="+"\"radio\""+ "name="+"\"sex\""+" value="+"\"female\""+" /> Excellent"+
		"<br /> " + 
		"<input type="+"\"radio\""+ "name="+"\"sex\""+" value="+"\"female\""+" /> Good"+
		"<br /> " + 
		"<input type="+"\"radio\""+ "name="+"\"sex\""+" value="+"\"female\""+" /> Fair"+
		"<br /> " + 
		"<input type="+"\"radio\""+ "name="+"\"sex\""+" value="+"\"female\""+" /> Bad"+
		"</form>" + 
		"</body> </html>"
		)
	return HttpResponse(html)

def current_datetime(request):
	now = datetime.datetime.now()
	t = get_template('cur.html')
	html = t.render(Context({'cur': now}))
	return HttpResponse(html)
