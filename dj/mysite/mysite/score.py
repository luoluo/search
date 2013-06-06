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
	r = c.execute('select * from doc')
	rowss = r.fetchall()
	t = get_template('score.html')
	html = ""
	for rows in rowss:
		if 'q' in request.GET:
			ss = request.GET['q']
			dd = re.match(r'.*(\d).*',ss)
			rr = re.match(r'\d(.*)', ss)
			dd = dd.group(1)
			rr = rr.group(1)
			c.execute('update doc set score = ? where name = ?', (int(dd), rr))
			conn.commit()

		html = html +(t.render(Context({'qname': rows[0],
								  'row1': rows[1] ,
								  'row2': rows[2] ,
								  'row3': rows[3] ,
								  'row4': rows[4] ,
								  'row5': rows[5] ,
								  'row6': rows[7] ,
								  'row7': rows[6]}
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
