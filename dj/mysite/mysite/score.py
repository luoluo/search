from django.http import HttpResponse
import re
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context
from django import forms
from mysite.form import ContactForm
import datetime
import sqlite3
import sys

def hello(request):
	conn = sqlite3.connect("re2")
	c = conn.cursor()
	if 'q' in request.GET:
		ss = request.GET['q']

		dd = re.match(r'(\d)%.*%\d',ss)
		if dd:
			dd = dd.group(1)
			
		rr = re.match(r'\d%(.*)%\d', ss)
		if rr:
			rr = rr.group(1)

		ee = re.match(r'\d%.*%(\d)', ss)
		if ee:
			ee = ee.group(1)
		else:
			ee = 6
		
		ee = str(int(ee)+1)
#		end = unicode(ee + 1)
		c.execute('update doc set score = ? where name = ?', (int(dd), rr))
		conn.commit()
		r = c.execute('select * from doc where id = ?', (ee))
		html = ee
	else:
		r = c.execute('select * from doc where id = 0')
		html = ""
	rows = r.fetchone()
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

def contact(request):
	t = get_template('form.html')
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			return HttpResponseRedirect('/search/')
	return HttpResponse('search')

def current_datetime(request):
	now = datetime.datetime.now()
	t = get_template('cur.html')
	html = t.render(Context({'cur': now}))
	return HttpResponse(html)

def search_form(request):
	return render_to_response('search_form.html')

def search(request):
	if 'q' in request.GET:
		message = 'You give score: %s.' % request.GET['q']
	else:
		message = 'You submit empty form.'
	return HttpResponse(message)
