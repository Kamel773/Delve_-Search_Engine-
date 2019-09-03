#-*-coding: utf-8 -*-
import sys
import csv
import time
import re
import random
from bs4 import BeautifulSoup
from pprint import pprint
from random import randint
import urllib2
import urllib
import json
import requests

def getUserAgent():
	user_agents = 'Just for academic purpose v'+str(random.uniform(11, 21))
	return user_agents

def quoralist_ext(csvw,count):
	site_html = urllib2.urlopen('file:///home/akujuou/Documents/DRSCrawlFile/Files/quoralist.html')
	soup = BeautifulSoup(site_html)
	s_link = soup.find_all("a","external_link")
	if s_link:
		for link in s_link:
			record = []
			record.append('N_A')
			record.append('DATA'+str(count))
			record.append('')
			record.append(link['href'])
			record.append('')
			csvw.writerow(record)
			count = count + 1
	print "total dataset gotten so far  -  quora list: "+str(count - 1699)
	return count
	
def stacklist_ext(csvw,count):
	site_html = urllib2.urlopen('file:///home/akujuou/Documents/DRSCrawlFile/Files/stacklist.html')
	soup = BeautifulSoup(site_html)
	answers = soup.find_all("div","post-text")
	if answers:
		for answer in answers:
			s_link = answer.find_all("a")
			if s_link:
				for link in s_link:
					record = []
					record.append('N_A')
					record.append('DATA'+str(count))
					record.append('')
					record.append(link['href'])
					record.append('')
					csvw.writerow(record)
					count = count + 1
	print "total dataset gotten so far  -  stack list: "+str(count - 1699)
	return count
	
def refdata_mine(csvw,count):
	url = 'http://www.re3data.org/api/beta/repositories'
	request = urllib2.Request(url, None, {'User-Agent':'Mosilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11'})
	site_html = urllib2.urlopen(request,timeout=30)
	soup = BeautifulSoup(site_html,'xml')
	s_links= soup.find_all('link')
	for links in s_links:
		url = links['href']
		if url:
			rep_html = urllib2.urlopen(url)
			rep_soup = BeautifulSoup(rep_html,'xml')
			record = []
			record.append('N_A')
			record.append('DATA'+str(count))
			try:
				record.append(rep_soup.repositoryName.string.replace("\n"," ").replace("\r"," ").replace("\t"," "))
			except:
				record.append('')
			record.append(rep_soup.repositoryURL.string)
			try:
				record.append(rep_soup.description.string.replace("\n"," ").replace("\r"," ").replace("\t"," "))
			except:
				record.append('')
			csvw.writerow(record)
			count = count + 1
			time.sleep(randint(1,2))
	print "total dataset gotten so far  -  redata: "+str(count - 1699)
	return count

def user_content(csvw,count):
	with open('Files/gitusercontent.csv','rU') as csvfile:
		reader = csv.reader(csvfile, delimiter=',', quotechar='|')
		for row in reader:
			record = []
			record.append('N_A')
			record.append('DATA'+str(count))
			record.append('')
			record.append(row[5])
			record.append('')
			csvw.writerow(record)
			count = count + 1
	with open('Files/Chicago.txt','rU') as csvfile:
		reader = csv.reader(csvfile, delimiter='\t', quotechar='|')
		for row in reader:
			record = []
			record.append('N_A')
			record.append('DATA'+str(count))
			try:
				record.append(row[0].replace("\n"," ").replace("\r"," ").replace("\t"," "))
			except:
				record.append('')
			record.append(row[2])
			try:
				record.append(row[3].replace("\n"," ").replace("\r"," ").replace("\t"," "))
			except:
				record.append('')
			csvw.writerow(record)
			count = count + 1
	url = 'http://kevinchai.net/datasets'
	request = urllib2.Request(url, None, {'User-Agent':'Mosilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11'})
	site_html = urllib2.urlopen(request,timeout=30)
	soup = BeautifulSoup(site_html)
	s_links= soup.find('div','entry-content').find_all('a')
	if s_links:
		for link in s_links:
			try:
				record = []
				record.append('N_A')
				record.append('DATA'+str(count))
				record.append('')
				record.append(link['href'])
				record.append('')
				csvw.writerow(record)
				count = count + 1
			except:
				print "item error"

	print "total dataset gotten so far  -  user contents: "+str(count - 1699)
	return count

def okfn_mine(csvw,count):
	url = 'http://data.okfn.org/data'
	request = urllib2.Request(url, None, {'User-Agent':'Mosilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11'})
	site_html = urllib2.urlopen(request,timeout=30)
	soup = BeautifulSoup(site_html)
	s_links= soup.find_all('div','dataset summary')
	for link in s_links:
		record = []
		record.append('N_A')
		record.append('DATA'+str(count))
		try:
			record.append(link.find('h3').find('a').text.replace("\n"," ").replace("\r"," ").replace("\t"," "))
		except:
			record.append('')
		record.append('http://data.okfn.org'+link.find('h3').find('a')['href'])
		descrp=link.find('div','description')
		try:
			record.append(descrp.string.replace("\n"," ").replace("\r"," ").replace("\t"," "))
		except:
			record.append('')
		csvw.writerow(record)
		count = count + 1
	print "total dataset gotten so far  -  okfn: "+str(count - 1699)
	return count
	
def opendatasoft(csvw,count):
	url = 'https://data.opendatasoft.com/api/datasets/1.0/search/?rows=-1'
	site_html = requests.get(url,headers={'User-Agent':'Mosilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11'})
	j_obj = json.loads(site_html.text)
	for dataset in j_obj['datasets']:
		record = []
		record.append('N_A')
		record.append('DATA'+str(count))
		try:
			record.append(dataset['metas']['title'].replace("\n"," ").replace("\r"," ").replace("\t"," "))
		except:
			record.append('')
		
		try:
			ref= dataset['metas']['references']
			if ref:
				record.append(ref)
			else:
				record.append('https://'+dataset['metas']['source_domain_address']+'/explore/dataset/'+dataset['metas']['source_dataset'])
		except:
			record.append('https://'+dataset['metas']['source_domain_address']+'/explore/dataset/'+dataset['metas']['source_dataset'])
		try:
			record.append(dataset['metas']['description'].replace("\n"," ").replace("\r"," ").replace("\t"," "))
		except:
			record.append(" ")

		csvw.writerow(record)
		count = count + 1;
	print "total dataset gotten so far  -  opendatasoft: "+str(count - 1699)
	return count

def reddit(csvw,count):
	listed = 0
	visit_pages = 0
	headers = {'User-Agent': getUserAgent()}
	url ='https://www.reddit.com/r/datasets/new/.json'
	site_html = requests.get(url,headers=headers,verify=False, timeout = 30)
	j_obj = json.loads(site_html.text)
	#init = j_obj['data']['children'][0]['data']['name']
	init = 't3_5r8xge'
	next= j_obj['data']['after']
	prog = re.compile('http[\w\./\-\?\:]+')
	while next != 'null':
		print "item count: "+str(listed)+" | next: "+str(next)
		req_quest = []
		results = j_obj['data']['children']
		for result in results:
			text_type = result['data']['link_flair_css_class']
			if text_type == 'dataset' or text_type == 'api' or text_type == 'null':
				if result['data']['domain'] == 'self.datasets':
					urls = prog.findall(result['data']['selftext'] )
					for url in urls:
						record = []
						record.append('N_A')
						record.append('DATAs'+str(count))
						record.append('')
						record.append(url)
						record.append('')
						csvw.writerow(record)
						count = count + 1
				else:
					record = []
					record.append('N_A')
					record.append('DATAs'+str(count))
					try:
						record.append(result['data']['title'].replace("\n"," ").replace("\r"," ").replace("\t"," "))
					except:
						record.append('')
					record.append(result['data']['url'])
					record.append('')
					csvw.writerow(record)
					count = count + 1
			elif text_type == 'question' or text_type == 'request':
				req_quest.append(result['data']['url'])
		for page in req_quest:
			sub_url = page+'.json'
			print sub_url
			time.sleep(randint(3,5))
			try:
				sub_site_html = requests.get(sub_url,headers=headers,verify=False, timeout = 30)
				sub_j_obj = json.loads(sub_site_html.text)
				comments = sub_j_obj[1]['data']['children']
				for comment in comments:
					try:
						urls = prog.findall(comment['data']['body'])
						for url in urls:
							record = []
							record.append('N_A')
							record.append('DATAs'+str(count))
							record.append('')
							record.append(url)
							try:
								record.append(sub_j_obj[0]['data']['children'][0]['data']['title'].replace("\n"," ").replace("\r"," ").replace("\t"," "))
							except:
								record.append('')
							csvw.writerow(record)
							count = count + 1
					except:
						print "Ops something went wrong...well, lose some... win some"
			except:
				print "Ops something went wrong...well, lose some... win some"

		time.sleep(randint(3,5))
		listed = listed + 25
		url ='https://www.reddit.com/r/datasets/new/.json?count='+str(listed)+'&after='+str(next)
		print url
		site_html = requests.get(url,headers=headers,verify=False, timeout = 30)
		j_obj = json.loads(site_html.text)
		next= j_obj['data']['after']
		visit_pages = visit_pages + 1
		print visit_pages
		if visit_pages == 15:
			break
	#count = reddit_update(csvw,count, init)
	print "total dataset gotten so far  -  redit: "+str(count - 1699)
	return count

def reddit_update(csvw,count, init):
	headers = {'User-Agent': getUserAgent()}
	listed = 0
	visit_pages = 0
	url ='https://www.reddit.com/r/datasets/new/.json?'
	site_html = requests.get(url,headers=headers,verify=False, timeout = 30)
	j_obj = json.loads(site_html.text)
	if len(j_obj['data']['children']) > 0:
		init = j_obj['data']['children'][0]['data']['name']
		before= j_obj['data']['before']
		prog = re.compile('http[\w\./\-\?\:]+')
		while before != 'null':
			print "item count: "+str(listed)+" | before: "+str(before)
			req_quest = []
			results = j_obj['data']['children']
			for result in results:
				text_type = result['data']['link_flair_css_class']
				if text_type == 'dataset' or text_type == 'api' or text_type == 'null':
					if result['data']['domain'] == 'self.datasets':
						urls = prog.findall(result['data']['selftext'] )
						for url in urls:
							record = []
							record.append('N_A')
							record.append('DATAs'+str(count))
							record.append('')
							record.append(url)
							record.append('')
							csvw.writerow(record)
							count = count + 1
					else:
						record = []
						record.append('N_A')
						record.append('DATAs'+str(count))
						try:
							record.append(result['data']['title'].replace("\n"," ").replace("\r"," ").replace("\t"," "))
						except:
							record.append('')
						record.append(result['data']['url'])
						record.append('')
						csvw.writerow(record)
						count = count + 1
				elif text_type == 'question' or text_type == 'request':
					req_quest.append(result['data']['url'])
			for page in req_quest:
				time.sleep(randint(3,5))
				try:
					sub_url = page+'.json'
					sub_site_html = requests.get(sub_url,headers=headers,verify=False, timeout = 30)
					sub_j_obj = json.loads(sub_site_html.text)
					comments = sub_j_obj[1]['data']['children']
					for comment in comments:
						try:
							urls = prog.findall(comment['data']['body'])
							for url in urls:
								record = []
								record.append('N_A')
								record.append('DATA'+str(count))
								record.append('')
								record.append(url)
								try:
									record.append(sub_j_obj[0]['data']['children'][0]['data']['title'].replace("\n"," ").replace("\r"," ").replace("\t"," "))
								except:
									record.append('')
								csvw.writerow(record)
								count = count + 1
						except:
							print "Ops something went wrong...well, lose some... win some"
				except:
					print "Ops something went wrong...well, lose some... win some"
			time.sleep(randint(3,5))
			listed = listed + 25
			before_bef = 'null'
			while before_bef == 'null':
				time.sleep(randint(43200,46200))
				url ='https://www.reddit.com/r/datasets/new/.json?count='+str(listed)+'&before='+str(before)
				print url
				site_html = requests.get(url,headers=headers,verify=False, timeout = 30)
				j_obj = json.loads(site_html.text)
				before = j_obj['data']['before']
				before_bef = before
			visit_pages = visit_pages + 1
			print "update "+str(visit_pages)

	return count

reload(sys) 
sys.setdefaultencoding('utf8')
fp = open('Files/extensivedata2.csv', 'a')
csvw = csv.writer(fp, delimiter = '\t')
count = 12500
#count = quoralist_ext(csvw,count)
#count = stacklist_ext(csvw,count)
#count = refdata_mine(csvw,count)
#count = user_content(csvw,count)
#count = okfn_mine(csvw,count)
#count = opendatasoft(csvw,count)
count = reddit(csvw,count)
fp.close()
