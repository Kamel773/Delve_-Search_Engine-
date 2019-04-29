# -*- coding: utf-8 -*-
import nltk.data
import os
import re

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

file = os.path.join('08530735.txt')
fp = open("08530735.txt", "r")
#print(fp.read())
symbols = ['-','=',')','(','{','}','%','$','#','@','^','±','*','+',',','/']
sentences = split_into_sentences(fp.read())
for sentence in sentences:
	for word in sentence.split():
		#print(word)
		word = word.lower()
		if (bool(re.match('[a-z]+[0-9]', word))):
			#print(word)
			foundit = False
			if len(word) <= 3:
				continue
			if word[-1:] == '.':
				word = word.replace('.','')
			if word[-2:].isdigit():
				continue
			for symbol in symbols:
				if symbol in word:
					#print(symbol)
					foundit = True
					break
			if foundit is not True:
				print(word)
	#print(sentence)
'''
# Extructing the sentance that mention a referance.
listofReferences = []
i = 0
for sentence in sentences:
	if 'REFERENCES' in sentence:
		break
	for i in range(100):
		referance = '[' + str(i) + ']'
		if referance in sentence:
			#print(sentence)
			listofReferences.append(sentence)
listofReferences = list(dict.fromkeys(listofReferences))
for re in listofReferences:
	print(re)
'''




# Delve_-Search_Engine-
