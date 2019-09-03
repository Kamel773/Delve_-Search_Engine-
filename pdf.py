import PyPDF2 
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re


pdfFileObj = open('08453118.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

num_pages = pdfReader.numPages

pageObj = pdfReader.getPage(7)
info = pageObj.extractText()
#info =  u" ".join(info.replace(u"\xa0", u" ").strip().split())
#print(info)
cleanText = ""
for myWord in info:
	if myWord != '\n':
		cleanText += myWord
	text = cleanText.split()
	print(text)

'''
for page in range(num_pages):
	pageObj = pdfReader.getPage(page)
	info = pageObj.extractText()
	urls = re.findall('(?P<url>https?://[^\s]+)', info)
	print(urls)
'''
