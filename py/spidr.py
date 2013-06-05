#!/usr/bin/python
#encoding:utf-8
import time
import urllib2
import re
import pymongo
import HTMLParser
#db = pymongo.Connection('localhost', 27017)
url2 = 'http://m.baidu.com/s?st=10a001&tn=webmkt&pre=web_am_index&word='

queriesBook = open("result")
while True :
	i = queriesBook.readline();
	if len(i) == 0:
		break
	
	temp = re.match(r'.*=(.*),.*', i)
	query = temp.group(1)
	print "\n\n" + query + "\n"
#	print query 

	url5 = url2 + "" + query
	f = urllib2.urlopen(url5) #the web page infomation is in html
	html = f.read()
	time.sleep(1)   
	#html = unicode(html, "gb2312").encode("utf8")
	
	####   To match ####
	name = re.compile(r'h4>(.*)')
	size = re.compile(r'.*MB.*')
	version = re.compile(r'.*(软件版本.*)')
	date = re.compile(r'.*(更新日.*)')
	download = re.compile(r'.*(下载次数.*)')
	link = re.compile(r'img.*(src="http:[\w\W]*)alt.*"')
	link2description = re.compile(r'.*class=.*list-a.*href="(.*)"')
#data-package="com.tencent.mobileqq"
	package = re.compile(r'.*data-package="(.*?)"')
#	link2description = re.compile(r'href="(.*)"')     #why not work??
#<meta name="description" content="手机QQ是由腾讯公司打造的移动互联网应用，提供免费的多媒体沟通服务，方便用户在移动设备上通过语音、图片、视频等方式轻松交流。手机QQ，只想与你更接近。" />
	description = re.compile(r'.*description.*"(.*)"')
			#<img src="http://hiphotos.baidu.com/wisegame/pic/item/fd2f070828381f309e45f8e6a8014c086e06f025.jpg" id="app-logo" alt="QQ"">
	
	lines = html.split('<')
	rp = ""
	for line in lines:
#		print line
		
		match = link2description.match(line)  
		if match:
#			print match.group(1)
			sf = urllib2.urlopen(match.group(1))	
			time.sleep(1)
			shtml = sf.read()
#			print shtml
			slines = shtml.split('\n')
			for sline in slines:
				match = description.match(sline)
				if match:
					print rp
					rp =  "description\t" + match.group(1) + "\t"

				match = package.match(sline)
				if match:
					rp  = rp + "package\t" + match.group(1) + "\t"
					break
			sf.close()
		
		match = name.match(line)  
		if match:
			rp = match.group(1) + "\t" +  rp
	
		match = version.match(line) 
		if match:
			rp = rp + match.group(1)
	
		match = date.match(line)   
		if match:
			rp = rp + match.group(1)
	
		match = download.match(line)   
		if match:
			rp = rp + match.group(1)
	
		match = link.match(line)
		if match:
			rp = rp + match.group(1)

	f.close()
queriesBook.close()
