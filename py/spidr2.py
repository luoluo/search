#!/usr/bin/python
#encoding:utf-8
import time
import urllib2
import re
import pymongo
import HTMLParser
import simplejson
#db = pymongo.Connection('localhost', 27017)
urlstart = 'http://estoresrvice7.dianapk.qihang.us/api/search/?clientid=rvtfeil_1&source=rvt_1&q='
urlend = '&start=0&count=10'

queriesBook = open("result")
while True :
	i = queriesBook.readline();
	if len(i) == 0:
		break
	
	temp = re.match(r'.*=(.*),.*', i)
	query = temp.group(1)
	print "\n\n" + query + "\n"
#	print query 

	url5 = urlstart + "" + query + urlend
	f = urllib2.urlopen(url5) #the web page infomation is in html
#	html = f.read()
#	print html	 
#	print html	 json str
	
	jdata = simplejson.load(f)
#	print jdata['errorCode']
#	print jdata['query']
	for i in range(0, 10):
		idata = simplejson.loads(jdata['items'][i]['caption'])
	#	idata = simplejson.dumps(jdata['items'][0]['caption'])
	#	print  jdata['items'][0]
		print  "name\t" + idata["name"].encode("utf8")
		print  "description\t" + idata["description"].encode("utf8")
		print	"icon_url\t" + idata["icon_url"]
		print	"download_count\t" + str(idata["download_count"])
		print	"size\t" + str(idata["size"]).encode("utf8")
#		print	"size\t" + idata["size"]
		print	"version\t" + idata["version"].encode("utf8")
#		print	"update_date\t" + str(idata["update_date"])
		print	"update_date\t" + time.strftime("%Y-%m-%d %X",time.gmtime(idata["update_date"]))
#	print jdata['items'][0]['caption'][0]
#	print jdata['items'][0]['caption'][1]
#	print jdata['items'][0]['caption'][2]
#	print jdata['items'][0]['caption'][3]
#	print jdata['items'][0]['caption'][4]
#	print jdata['items'][1]
#	print jdata['items'][2]
#	print jdata['items']['caption']
#	print jdata[2]
#	print jdata[3]
#	print jdata[4]
#	print jdata[5]
#	print jdata[6]
####   To Match ###########

#	time.sleep(1)   
	#html = unicode(html, "gb2312").encode("utf8")
	
	####   To match ####
#{"query":"qq"
#"items":[{"score":294.83688
#"caption":"{\"id\":27117
#\"name\":\"QQ浏览器\"
#\"description\":\"QQ浏览器是腾讯公司QQ系列经典产品之一，让您最快的速度冲浪互联网！\\r\\n功能简介：\\r\\n1、通过www中转，数据压缩等方式\"
#\"icon_url\":\"http://estoredwnld7.189store.com/img/full/f/eb/feb7ce42e5b8604a663a2c459d993aa11c344814.png\"
#\"rate\":4.5
#\"download_count\":41852901
#\"display_download_count\":\"4185万+\"
#\"size\":\"8.5M\"
#\"original_size\":8882817
#\"version\":\"4.2\"
#\"version_code\":\"420430\"
#\"update_date\":1369705802
#\"package_name\":\"com.tencent.mtt\"
#\"min_sdk_version\":7
#\"max_sdk_version\":9223372036854775807
#\"category_id\":\"14334\"
#\"platform\":\"[1]\"
#\"app_type\":0}"}
#	name = re.compile(r'\\"name.*?".*?"(.*)\\"')
#	size = re.compile(r'.*MB.*')
#	version = re.compile(r'.*(软件版本.*)')
#	date = re.compile(r'.*(更新日.*)')
#	download = re.compile(r'.*(下载次数.*)')
#	link = re.compile(r'icon.*"(http:[\w\W]*).*"')
	#<img src="http://hiphotos.baidu.com/wisegame/pic/item/fd2f070828381f309e45f8e6a8014c086e06f025.jpg" id="app-logo" alt="QQ"">
	
#	lines = html.split(',')
#	for line in lines:
##		print line
#		
#		match = name.match(line)  
#		if match:
#			print match.group(1)
#	
#		match = version.match(line) 
#		if match:
#			print match.group(1)
#	
#		match = date.match(line)   
#		if match:
#			print  match.group(1)
#	
#		match = download.match(line)   
#		if match:
#			print match.group(1)
#	
#		match = link.match(line)
#		if match:
#			print match.group(1)
	f.close()
queriesBook.close()
