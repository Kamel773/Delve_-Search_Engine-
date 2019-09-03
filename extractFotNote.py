from bs4 import BeautifulSoup
import re
import nltk.data
import os
import glob
import pickle
import csv
import glob, multiprocessing
from threading import Lock, Thread
import time
'''
"Beautiful code must be short", Adam Kolawa.
'''

pickleFile = open("/home/rashedka/Desktop/FinalExtracting/DelveXML/listXMLfile_Delve_XML.p",'rb')
fileAlreadyExtracted = pickle.load(pickleFile)

alphabets= "([A-Za-z])"
prefixes = "(Mr|St|Mrs|Ms|Dr)[.]"
suffixes = "(Inc|Ltd|Jr|Sr|Co)"
starters = "(Mr|Mrs|Ms|Dr|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|et al.|\sWherever)"
acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
websites = "[.](com|net|org|io|gov)"

def split_into_sentences(text):
    text = " " + str(text) + "  "
    text = text.replace("\n"," ")
    for checkingHttp in text.split():
    	if 'http' in checkingHttp:
    		text = text.replace(checkingHttp,checkingHttp.replace(".","<prd>"))
    	#if checkingHttp[-5:].endswith('<prd>'):
    		#print(checkingHttp)
    		#text = text.replace(checkingHttp,checkingHttp.replace("<prd>",".")) + '.'
    	if bool(re.match('^[0-9.%]+%', checkingHttp)):
    		text = text.replace(checkingHttp,checkingHttp.replace(".","<prd>"))
    	#if bool(re.match('^[0-9.]', checkingHttp)):
    		#print(checkingHttp)

    text = text.replace("et al.","et al")
    text = re.sub(prefixes,"\\1<prd>",text)
    text = re.sub(websites,"<prd>\\1",text)
    if "Ph.D" in text: text = text.replace("Ph.D.","Ph<prd>D<prd>")
    text = re.sub("\s" + alphabets + "[.] "," \\1<prd> ",text)
    text = re.sub(acronyms+" "+starters,"\\1<stop> \\2",text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>\\3<prd>",text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>",text)
    text = re.sub(" "+suffixes+"[.] "+starters," \\1<stop> \\2",text)
    text = re.sub(" "+suffixes+"[.]"," \\1<prd>",text)
    text = re.sub(" " + alphabets + "[.]"," \\1<prd>",text)
    if "\"" in text: text = text.replace(".\"","\".")
    if "!" in text: text = text.replace("!\"","\"!")
    if "?" in text: text = text.replace("?\"","\"?")
    text = text.replace(".",".<stop>")
    #text = text.replace("?","?<stop>")
    #text = text.replace("!","!<stop>")
    text = text.replace("<prd>",".")
    sentences = text.split("<stop>")
    sentences = sentences[:-1]
    sentences = [s.strip() for s in sentences]
    return sentences

#// Reading the XML file
outputCSV = open('extractingFootNoteSentence.csv', mode='w')
outputCSV_writer = csv.writer(outputCSV, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

listXMLfile = []
count = 0
path = '/home/rashedka/Desktop/Delve_XML/'
for filename in glob.glob(os.path.join(path,'*.xml')):
	#Extracting the file name
	start = '/home/rashedka/Desktop/Delve_XML/'
	end = '.tei.xml'
	filenameXML = (filename.split(start))[1].split(end)[0]
	if filenameXML in fileAlreadyExtracted:
		#print(filenameXML)
		continue
	#print(filenameXML)
	xmlfile = open(filename,'r')
	contents = xmlfile.read()
	t2_soup = None
	count = count + 1
	dic = {}
	
	soup = BeautifulSoup(contents, "html5lib")
	data = ''
	for note in soup.find_all('note'):
		try:
			if note.attrs['place'] != 'foot':
				continue
		except:
			continue
		try:
			if (len(note.get_text().split())) == 1:
				footNote = note.attrs['n'] + ' ' + note.get_text()
				dic[note.attrs['n']] = note.get_text()
			if (len(note.get_text().split())) > 1:
				footNote = note.attrs['n'] + ' ' + note.get_text()
				for word in footNote.split():
					#if word[:5] == 'https':
					if 'htt' in word:
						data = data + word + ' '
					if word.isdigit():
						data = data + word + ' '
				for multi in data.split():
					if multi.isdigit():
						key = multi
						continue
					dic[key] = multi
					listXMLfile.append(filenameXML)
					outputCSV_writer.writerow([filenameXML, dic[key]])
					print(count)
					
		except:
			continue
	#print(dic)
	

	'''
	#// extracting the sentance 
	cleanSentence = None
	sentences = split_into_sentences(contents)
	for sentence in sentences:
		for key in dic:
			query = '<ref type="bibr" target="#b0">' + key +'</ref>'
			if query in sentence:
				print('---')
				cleanSentence = BeautifulSoup(sentence, "html5lib")
				print(cleanSentence.get_text())
				cleanSentence = cleanSentence.get_text()
				print(dic[key])
				print(count)
				print(dic)
				listXMLfile.append(filenameXML)
				outputCSV_writer.writerow([filenameXML, dic[key], cleanSentence])
	'''
	





#print(listXMLfile)
pickle.dump(listXMLfile, open( "listXMLfile.p", "wb" ) )





'''
from bs4 import BeautifulSoup
import re
import nltk.data
import os
import glob
import pickle
import csv


alphabets= "([A-Za-z])"
prefixes = "(Mr|St|Mrs|Ms|Dr)[.]"
suffixes = "(Inc|Ltd|Jr|Sr|Co)"
starters = "(Mr|Mrs|Ms|Dr|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|et al.|\sWherever)"
acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
websites = "[.](com|net|org|io|gov)"

def split_into_sentences(text):
    text = " " + str(text) + "  "
    text = text.replace("\n"," ")
    for checkingHttp in text.split():
    	if 'http' in checkingHttp:
    		text = text.replace(checkingHttp,checkingHttp.replace(".","<prd>"))
    	#if checkingHttp[-5:].endswith('<prd>'):
    		#print(checkingHttp)
    		#text = text.replace(checkingHttp,checkingHttp.replace("<prd>",".")) + '.'
    	if bool(re.match('^[0-9.%]+%', checkingHttp)):
    		text = text.replace(checkingHttp,checkingHttp.replace(".","<prd>"))
    	#if bool(re.match('^[0-9.]', checkingHttp)):
    		#print(checkingHttp)

    text = text.replace("et al.","et al")
    text = re.sub(prefixes,"\\1<prd>",text)
    text = re.sub(websites,"<prd>\\1",text)
    if "Ph.D" in text: text = text.replace("Ph.D.","Ph<prd>D<prd>")
    text = re.sub("\s" + alphabets + "[.] "," \\1<prd> ",text)
    text = re.sub(acronyms+" "+starters,"\\1<stop> \\2",text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>\\3<prd>",text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>",text)
    text = re.sub(" "+suffixes+"[.] "+starters," \\1<stop> \\2",text)
    text = re.sub(" "+suffixes+"[.]"," \\1<prd>",text)
    text = re.sub(" " + alphabets + "[.]"," \\1<prd>",text)
    if "\"" in text: text = text.replace(".\"","\".")
    if "!" in text: text = text.replace("!\"","\"!")
    if "?" in text: text = text.replace("?\"","\"?")
    text = text.replace(".",".<stop>")
    #text = text.replace("?","?<stop>")
    #text = text.replace("!","!<stop>")
    text = text.replace("<prd>",".")
    sentences = text.split("<stop>")
    sentences = sentences[:-1]
    sentences = [s.strip() for s in sentences]
    return sentences

#// Reading the XML file
outputCSV = open('extractingFootNoteSentence.csv', mode='w')
outputCSV_writer = csv.writer(outputCSV, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

listXMLfile = []
count = 0
path = '/home/rashedka/Desktop/Delve_XML/'
for filename in glob.glob(os.path.join(path,'*.xml')):
	#Extracting the file name
	start = '/home/rashedka/Desktop/Delve_XML/'
	end = '.tei.xml'
	filenameXML = (filename.split(start))[1].split(end)[0]
	#print(filenameXML)
	xmlfile = open(filename,'r')
	contents = xmlfile.read()
	t2_soup = None
	count = count + 1
	dic = {}
	
	soup = BeautifulSoup(contents, "html5lib")
	data = ''
	for note in soup.find_all('note'):
		try:
			if note.attrs['place'] != 'foot':
				continue
		except:
			continue
		try:
			if (len(note.get_text().split())) == 1:
				footNote = note.attrs['n'] + ' ' + note.get_text()
				dic[note.attrs['n']] = note.get_text()
			if (len(note.get_text().split())) > 1:
				footNote = note.attrs['n'] + ' ' + note.get_text()
				for word in footNote.split():
					#if word[:5] == 'https':
					if 'htt' in word:
						data = data + word + ' '
					if word.isdigit():
						data = data + word + ' '
				for multi in data.split():
					if multi.isdigit():
						key = multi
						continue
					dic[key] = multi
					
		except:
			continue
	#print(dic)
	
	#// extracting the sentance 
	cleanSentence = None
	sentences = split_into_sentences(contents)
	for sentence in sentences:
		for key in dic:
			query = '<ref type="bibr" target="#b0">' + key +'</ref>'
			if query in sentence:
				print('---')
				cleanSentence = BeautifulSoup(sentence, "html5lib")
				print(cleanSentence.get_text())
				cleanSentence = cleanSentence.get_text()
				print(dic[key])
				print(count)
				print(dic)
				listXMLfile.append(filenameXML)
				outputCSV_writer.writerow([filenameXML, dic[key], cleanSentence])
	


print(listXMLfile)
pickle.dump(listXMLfile, open( "listXMLfile.p", "wb" ) )






'''