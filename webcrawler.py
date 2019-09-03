#-*-coding: utf-8 -*-
import sys
import csv
import time
from random import choice
from bs4 import BeautifulSoup
from pprint import pprint
from random import randint
import urllib2
import urllib


def Wikipediacrawl(url, csvw):
	external_sites_html = urllib2.urlopen(url)
	soup = BeautifulSoup(external_sites_html)
	links = soup.find_all("li")
	for link in links:
		s_link = link.find("a","external")
		if s_link:
			record = []
			record.append(s_link.text)
			record.append(s_link['href'])
			csvw.writerow(record)

def Biobankcrawl(url, csvw):
	external_sites_html = urllib2.urlopen(url)
	soup = BeautifulSoup(external_sites_html)
	links = soup.find_all("td")
	for link in links:
		s_link = link.find("a")
		if s_link:
			record = []
			record.append(s_link.text)
			record.append(s_link['href'])
			csvw.writerow(record)


def Nasa_Inf_crawl(url, csvw):
	external_sites_html = urllib2.urlopen(url)
	soup = BeautifulSoup(external_sites_html)
	links = soup.find_all("li")
	for link in links:
		s_link = link.find("a")
		if s_link:
			record = []
			record.append(s_link.text)
			record.append(s_link['href'])
			csvw.writerow(record)

def cmu_crawl(url, csvw):
	external_sites_html = urllib2.urlopen(url)
	soup = BeautifulSoup(external_sites_html)
	links = soup.find_all("li")
	for link in links:
		s_link = link.find("b").find("a")
		if s_link:
			record = []
			record.append(s_link.text)
			record.append(s_link['href'])
			csvw.writerow(record)

def git_crawl(url, csvw):
	external_sites_html = urllib2.urlopen(url)
	soup = BeautifulSoup(external_sites_html)
	links = soup.find("div","readme").find_all("li")
	for link in links:
		s_link = link.find("a")
		if s_link:
			record = []
			record.append(s_link.text)
			record.append(s_link['href'])
			csvw.writerow(record)


reload(sys) 
sys.setdefaultencoding('utf8')
fp = open('Files/linkcompile7.csv', 'a')
csvw = csv.writer(fp, delimiter = '\t')
url = 'https://github.com/caesar0301/awesome-public-datasets'
git_crawl(url, csvw)
fp.close()
