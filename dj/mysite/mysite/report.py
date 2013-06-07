from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context
from django import forms
import sqlite3
import sys

def report(request):
	conn = sqlite3.connect("rer2")
	c = conn.cursor()
	html = "<head> <body>"
	html = html + "query  doc  dcg  maxdcg  ndcg  rank"
	rowss = c.execute('select * from docr')
	if rowss == None:
		html = "We've done, thank you for voting!!!"
		return HttpResponse(html)
	t = get_template('report.html')
	for rows in rowss:
		html = html+ "<br>" +(t.render(Context({'iid':rows[0],
								  'row1': rows[1] ,
								  'row2': rows[2] ,
								  'row3': rows[3] ,
								  'row4': rows[4] ,
								  'row5': rows[5]}
			)))
#	http = http + "</body> </html>"
	return HttpResponse(html)
